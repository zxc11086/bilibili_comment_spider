# b站评论爬虫

## 介绍
通过 B 站关键词搜索视频，再批量抓取评论并写入文本文件。

## 运行环境
- Python 3.8+
- 无第三方依赖（仅使用标准库）

## 使用方法
### 交互模式
```bash
python main.py
```

### 命令行参数模式（推荐）
```bash
python main.py -k 科技 --search-pages 2 --sort 2 -o comments.txt
```

参数说明：
- `-k/--keyword`：关键词
- `--search-pages`：搜索结果抓取页数，默认 `1`
- `--sort`：评论排序，`0` 按时间，`2` 按热度
- `-o/--output`：输出文件路径，默认 `<关键词>.txt`

## 常见问题
- 如果接口返回风控/限流，可稍后重试，或减少抓取页数。
