# T-Youtube
A tools to download video, mp3, transcripts from Youtube

> Repo này để mình thực hành tạo `Docker`, mình sẽ chuyển cái tool python của mình sang docker để ai cũng có thể chạy được mà ko cần cài đặt các python packages ^^

Hướng dẫn về Docker

https://dothanhlong.org/huong-dan-docker-toan-tap/

https://colab.research.google.com/drive/1E4B0xMXFpcX13gpPTx4scNP_hRulNxPG

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

# Preferences

https://viblo.asia/p/docker-run-vs-cmd-vs-entrypoint-Az45boVgKxY

https://blog.cloud365.vn/container/tim-hieu-docker-phan-4/

https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile