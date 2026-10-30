#!/usr/bin/env python3
"""
抖音视频下载器
用法: python3 download_douyin.py "抖音链接"
"""
import requests
import re
import sys
import json

def download_douyin_video(url):
    """下载抖音视频"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
    }
    
    try:
        # 1. 获取真实链接
        resp = requests.get(url, headers=headers, allow_redirects=True, timeout=30)
        final_url = resp.url
        print(f"真实链接: {final_url}")
        
        # 2. 提取视频ID
        video_id_match = re.search(r'/(\d+)', final_url)
        if not video_id_match:
            print("❌ 无法提取视频ID")
            return None
        video_id = video_id_match.group(1)
        print(f"视频ID: {video_id}")
        
        # 3. 获取页面内容
        page_url = f"https://www.iesdouyin.com/share/video/{video_id}/"
        page_resp = requests.get(page_url, headers=headers, timeout=30)
        page_text = page_resp.text
        
        # 4. 提取视频URI
        uri_match = re.search(r'"play_addr":{"uri":"([^"]+)"', page_text)
        if not uri_match:
            print("❌ 无法找到视频资源")
            return None
        
        video_uri = uri_match.group(1)
        print(f"视频URI: {video_uri}")
        
        # 5. 下载视频
        video_url = f"https://aweme.snssdk.com/aweme/v1/play/?video_id={video_uri}&line=0&ratio=540p"
        video_resp = requests.get(video_url, headers=headers, timeout=120)
        
        if video_resp.status_code != 200 or len(video_resp.content) < 100000:
            print(f"❌ 下载失败: 状态码={video_resp.status_code}, 大小={len(video_resp.content)}")
            return None
        
        # 6. 保存文件
        filename = f"douyin_{video_id}.mp4"
        with open(filename, 'wb') as f:
            f.write(video_resp.content)
        
        print(f"✅ 下载完成: {filename} ({len(video_resp.content)/1024/1024:.2f} MB)")
        return filename
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        url = input("请输入抖音链接: ").strip()
    else:
        url = sys.argv[1]
    
    result = download_douyin_video(url)
    sys.exit(0 if result else 1)
