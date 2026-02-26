import argparse
import json
import urllib.request
from pathlib import Path
from typing import List

import search

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    )
}


def get_json(url: str, timeout: int = 10) -> dict:
    req = urllib.request.Request(url=url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # nosec B310
        return json.loads(resp.read().decode("utf-8"))


def crawl_video_comments(aid: int, sort: int = 2) -> List[str]:
    comments: List[str] = []
    page = 1

    while True:
        url = f"https://api.bilibili.com/x/v2/reply?pn={page}&type=1&oid={aid}&sort={sort}"
        try:
            data = get_json(url)
        except Exception as exc:
            print(f"[WARN] aid={aid} 第 {page} 页请求失败: {exc}")
            break

        if data.get("code") != 0:
            print(f"[WARN] aid={aid} 接口返回异常: {data.get('message')}")
            break

        payload = data.get("data") or {}
        replies = payload.get("replies") or []
        for item in replies:
            msg = (item.get("content") or {}).get("message")
            if msg:
                comments.append(msg)

        page_info = payload.get("page") or {}
        count = page_info.get("count", 0)
        size = page_info.get("size", 20) or 20
        total_pages = max(1, (count + size - 1) // size)

        if page >= total_pages:
            break
        page += 1

    return comments


def main() -> None:
    parser = argparse.ArgumentParser(description="B站关键词评论爬取")
    parser.add_argument("--keyword", "-k", help="搜索关键词，不传则交互输入")
    parser.add_argument("--search-pages", type=int, default=1, help="搜索结果抓取页数")
    parser.add_argument("--sort", type=int, default=2, choices=[0, 2], help="评论排序: 0时间 2热度")
    parser.add_argument("--output", "-o", help="输出文件路径，默认<关键词>.txt")
    args = parser.parse_args()

    keyword = args.keyword or input("请输入话题: ").strip()
    if not keyword:
        raise SystemExit("关键词不能为空")

    videos = search.search(keyword, pages=max(1, args.search_pages))
    print(f"搜索到 {len(videos)} 个视频")

    all_comments: List[str] = []
    for idx, (aid, bvid) in enumerate(videos, start=1):
        print(f"[{idx}/{len(videos)}] 抓取 {bvid} (aid={aid})")
        all_comments.extend(crawl_video_comments(aid=aid, sort=args.sort))

    out_path = Path(args.output or f"{keyword}.txt")
    out_path.write_text("\n".join(all_comments), encoding="utf-8")
    print(f"共写入 {len(all_comments)} 条评论 -> {out_path}")


if __name__ == "__main__":
    main()
