# T-Youtube
A tools to download video, mp3, transcripts from Youtube

> Docker hub

https://hub.docker.com/r/soiqualang/tyoutube

> Repo này để mình thực hành tạo `Docker`, mình sẽ chuyển cái tool python của mình sang docker để ai cũng có thể chạy được mà ko cần cài đặt các python packages ^^


## Setup Local

### Virtual Env

```bash
virtualenv tyoutube_env

pip install autosub
pip install pytube
pip install youtube_dl

pip freeze > requirements.txt
```

### Run tool

> Active Virtual Env

```bash
# Window
tyoutube_env/Scripts/activate

# Linux
source tyoutube_env/bin/activate
```

> Run tool

* `download_mode`: What you want to download
  * `video`: A video file
  * `mp3`: A mp3 file
  * `list`: List video in youtube playlist
* `youtube_url`: Youtube video or Playlist link
* `download_path`: Path to save video, mp3,..

```bash
# Download all video in a playlist
python tyb.py -download_mode "list" -youtube_url "PLhPvsstp6O2QTcrY20ysXRbyRo30am87X" -download_path "keochanh_mp3"
# or
python tyb.py -download_mode "list" -youtube_url "https://www.youtube.com/playlist?list=PLhPvsstp6O2QTcrY20ysXRbyRo30am87X" -download_path "keochanh_mp3"

# Download a video
python tyb.py -download_mode "video" -youtube_url "https://www.youtube.com/watch?v=tNfGBssfCmE" -download_path "keochanh_mp3"

# Download a mp3
python tyb.py -download_mode "mp3" -youtube_url "https://www.youtube.com/watch?v=tNfGBssfCmE" -download_path "keochanh_mp3"
```

## Use Docker

### Pull and start container

* `<your_local_download_dir>`: Your local dir that you want to save your video, mp3,..
* `<docker_download_dir>`: Download dir in docker

Ex: `docker run -it -d --name tyoutube -v D:/sync/websvr/docker/tmp:/data soiqualang/tyoutube:1.0`

```bash
# Pull and start container
docker run -it -d --name tyoutube -v <your_local_download_dir>:/<docker_download_dir> soiqualang/tyoutube:1.0

# Stop container
docker stop tyoutube

# Start container
docker start tyoutube

# Remove container
docker rm tyoutube
```

### Run tool

* `download_mode`: What you want to download
  * `video`: A video file
  * `mp3`: A mp3 file
  * `list`: List video in youtube playlist
* `youtube_url`: Youtube video or Playlist link
* `download_path`: Path to save video, mp3,..

```bash
# Download a file mp3
docker exec -it tyoutube python tyb.py -download_mode "mp3" -youtube_url "https://www.youtube.com/watch?v=tNfGBssfCmE" -download_path "/data/keochanh_mp3"

# Download a video
docker exec -it tyoutube python tyb.py -download_mode "video" -youtube_url "https://www.youtube.com/watch?v=tNfGBssfCmE" -download_path "keochanh_mp3"

# Download all video in a playlist
python tyb.py -download_mode "list" -youtube_url "PLhPvsstp6O2QTcrY20ysXRbyRo30am87X" -download_path "keochanh_mp3"
# or
python tyb.py -download_mode "list" -youtube_url "https://www.youtube.com/playlist?list=PLhPvsstp6O2QTcrY20ysXRbyRo30am87X" -download_path "keochanh_mp3"
```


# Preferences

https://viblo.asia/p/docker-run-vs-cmd-vs-entrypoint-Az45boVgKxY

https://blog.cloud365.vn/container/tim-hieu-docker-phan-4/

https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile