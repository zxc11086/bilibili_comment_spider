import json
import urllib.parse
import urllib.request
from typing import List, Tuple

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    )
}


def _get_json(url: str, timeout: int = 10) -> dict:
    req = urllib.request.Request(url=url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # nosec B310
        return json.loads(resp.read().decode("utf-8"))


def search(keyword: str, pages: int = 1) -> List[Tuple[int, str]]:
    """按关键词搜索视频，返回 (aid, bvid) 列表。"""
    result: List[Tuple[int, str]] = []
    seen = set()

    for page in range(1, pages + 1):
        params = urllib.parse.urlencode(
            {
                "search_type": "video",
                "keyword": keyword,
                "page": page,
                "order": "click",
            }
        )
        url = f"https://api.bilibili.com/x/web-interface/search/type?{params}"

        try:
            data = _get_json(url)
        except Exception as exc:
            print(f"[WARN] 搜索第 {page} 页失败: {exc}")
            continue

        if data.get("code") != 0:
            print(f"[WARN] 搜索接口返回异常: {data.get('message')}")
            continue

        for item in data.get("data", {}).get("result", []) or []:
            aid = item.get("aid")
            bvid = item.get("bvid")
            if not aid or not bvid:
                continue
            key = (aid, bvid)
            if key in seen:
                continue
            seen.add(key)
            result.append(key)

    return result
