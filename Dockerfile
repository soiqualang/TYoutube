FROM python:alpine AS base
WORKDIR /app
COPY requirements.txt .
COPY tyb.py .
RUN pip install -r requirements.txt

VOLUME ["/app"]
