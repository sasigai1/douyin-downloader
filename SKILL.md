---
name: douyin-downloader
description: Download Douyin (TikTok China) videos from share links. Use when user provides a Douyin URL or wants to download Douyin videos.
---

# Douyin Video Downloader

Download videos from Douyin (抖音) using share links.

## Usage

Provide a Douyin share link:
- Short URL: `https://v.douyin.com/xxxxxx/`
- Full URL: `https://www.douyin.com/video/xxxxxx`

## Workflow

1. User provides Douyin link
2. Run: `python3 skills/douyin-downloader/scripts/download_douyin.py "<url>"`
3. Video downloads to `douyin_<video_id>.mp4`

## Examples

**Download from short link:**
```bash
python3 skills/douyin-downloader/scripts/download_douyin.py "https://v.douyin.com/jCYGepVEl-Y/"
```

**Download and send to user:**
```bash
python3 skills/douyin-downloader/scripts/download_douyin.py "<url>"
message --filePath douyin_<id>.mp4
```

## Notes

- Works with iesdouyin.com and douyin.com links
- Downloads ~540p resolution by default
- Files saved in workspace root
- File naming: `douyin_<video_id>.mp4`
