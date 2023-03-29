import os
import requests
from tqdm import tqdm
import re

def download_video(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('Content-Length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=block_size):
                if chunk:
                    f.write(chunk)
                    progress_bar.update(len(chunk))
        progress_bar.close()
    return filename
def download_thumbnail(video_url):
    video_id = re.findall(r"v=([^&]+)", video_url)[0]
    api_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    response = requests.get(api_url)
    if response.status_code == 200:
        video_info = response.json()
        video_title = video_info["title"]
        thumbnail_url = video_info["thumbnail_url"]
        thumbnail_data = requests.get(thumbnail_url).content
        thumbnail_name = f"{video_title}.jpg"
        thumbnail_path = os.path.join("thumbnails", thumbnail_name)
        if not os.path.exists("thumbnails"):
            os.makedirs("thumbnails")
        with open(thumbnail_path, "wb") as f:
            f.write(thumbnail_data)
        print(f"Thumbnail saved as {thumbnail_path}")
    else:
        print(f"Error getting video info for {video_url}")