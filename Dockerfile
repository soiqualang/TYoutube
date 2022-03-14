FROM python:alpine AS py_base
WORKDIR /app
RUN apk add  --no-cache ffmpeg
COPY requirements.txt .
COPY tyb.py .
RUN pip install -r requirements.txt
RUN pip install -U youtube-dl
