FROM python:3

WORKDIR /usr/src/app/spider-works

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY crawler crawler
COPY ./go-spider.py ./
COPY ./scrapy.cfg ./
