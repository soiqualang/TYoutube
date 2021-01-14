# T-Youtube
A tools to download video, mp3, transcripts from Youtube

> Repo này để mình thực hành tạo `Docker`, mình sẽ chuyển cái tool python của mình sang docker để ai cũng có thể chạy được mà ko cần cài đặt các python packages ^^

Hướng dẫn về Docker

https://dothanhlong.org/huong-dan-docker-toan-tap/

Trong này mình vẫn còn vướng mắc:

* Làm sao để ghi file ra ngoài môi trường Docker (khi download video, mp3)
* Gọi lệnh vô môi trường Docker để chạy tool
* Có cần tạo `virtualenv` để cài các packages không, nếu có thì có dùng lại `virtualenv` ở local được không?

## Setup Local

### Virtual Env

```bash
virtualenv tyoutube_env

```