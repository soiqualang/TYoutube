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
docker run -it -d --name tyoutube -v D:/sync/websvr/docker/tmp:/data tyoutube:1.0
docker run -it -d --name tyoutube -v D:/sync/websvr/docker/tmp:/data soiqualang/tyoutube:1.0

# Stop container
docker stop tyoutube

# Start container
docker start tyoutube

# cli to container
docker exec -it tyoutube /bin/sh

# Thoát cli
`exit`

# Run tool
python tyb.py -download_mode "mp3" -youtube_url "https://www.youtube.com/watch?v=tNfGBssfCmE" -download_path "/data/keochanh_mp3"
python tyb.py -download_mode "video" -youtube_url "https://www.youtube.com/watch?v=tNfGBssfCmE" -download_path "/data/keochanh_mp3"

# Remove container
docker rm tyoutube
```

### Push to Dockerhub

```bash
docker login -u soiqualang
docker tag tyoutube:1.0 soiqualang/tyoutube:1.0
docker push soiqualang/tyoutube:1.0
```

# Preferences

https://viblo.asia/p/docker-run-vs-cmd-vs-entrypoint-Az45boVgKxY

https://blog.cloud365.vn/container/tim-hieu-docker-phan-4/

https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile