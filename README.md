# T-Youtube
A tools to download video, mp3, transcripts from Youtube

> Repo này để mình thực hành tạo `Docker`, mình sẽ chuyển cái tool python của mình sang docker để ai cũng có thể chạy được mà ko cần cài đặt các python packages ^^

Hướng dẫn về Docker

https://dothanhlong.org/huong-dan-docker-toan-tap/

https://colab.research.google.com/drive/1E4B0xMXFpcX13gpPTx4scNP_hRulNxPG

https://github.com/quangvublog/Docker/blob/master/Dockerfile

Trong này mình vẫn còn vướng mắc:

* Làm sao để ghi file ra ngoài môi trường Docker (khi download video, mp3)
* Gọi lệnh vô môi trường Docker để chạy tool
* Có cần tạo `virtualenv` để cài các packages không, nếu có thì có dùng lại `virtualenv` ở local được không?

## Setup Local

### Virtual Env

```bash
virtualenv tyoutube_env

pip install autosub
pip install pytube
pip install youtube_dl

pip freeze > requirements.txt
```

### Build tool

```bash
# List video
python tyb.py -download_mode "list" -youtube_url "PLhPvsstp6O2QTcrY20ysXRbyRo30am87X" -download_path "keochanh_mp3"
# hoặc
python tyb.py -download_mode "list" -youtube_url "https://www.youtube.com/playlist?list=PLhPvsstp6O2QTcrY20ysXRbyRo30am87X" -download_path "keochanh_mp3"

# a video
python tyb.py -download_mode "video" -youtube_url "https://www.youtube.com/watch?v=tNfGBssfCmE" -download_path "keochanh_mp3"

# a mp3
python tyb.py -download_mode "mp3" -youtube_url "https://www.youtube.com/watch?v=tNfGBssfCmE" -download_path "keochanh_mp3"
```

### Build Docker ra image

```bash
# Tên docker không được viết hoa
docker build -t tyoutube:1.0 .
```

### Run Docker

```bash
# Tạo và start container
docker run -it -v D:/sync/websvr/docker/tmp:/data c7f0c536649c

# Stop container
docker stop 4110d0e401c0

# Start container
docker start 4110d0e401c0

# cli to container
# Linux
docker exec -it 4110d0e401c0 /bin/bash
# Window
docker exec -it 4110d0e401c0 /bin/sh

# Run tool
python tyb.py -download_mode "mp3" -youtube_url "https://www.youtube.com/watch?v=tNfGBssfCmE" -download_path "/data/keochanh_mp3"
```

# Preferences

https://viblo.asia/p/docker-run-vs-cmd-vs-entrypoint-Az45boVgKxY

https://blog.cloud365.vn/container/tim-hieu-docker-phan-4/

https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile