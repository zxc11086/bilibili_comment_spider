# Bilibili Comment Crawler

## Introduction
Search for videos on Bilibili using keywords, then batch crawl comments and save them to a text file.

## Runtime Environment
- Python 3.8+
- No third-party dependencies (only standard library)

## Usage Methods
### Interactive Mode
```bash
python main.py
```

### Command-line Arguments Mode (Recommended)
```bash
python main.py -k 科技 --search-pages 2 --sort 2 -o comments.txt
```

Parameter descriptions:
- `-k/--keyword`: Keyword to search
- `--search-pages`: Number of search result pages to crawl, default `1`
- `--sort`: Comment sorting, `0` by time, `2` by popularity
- `-o/--output`: Output file path, default `<keyword>.txt`

## Common Issues
- If the API returns rate limiting or throttling responses, wait a bit and retry, or reduce the number of search pages to crawl.
