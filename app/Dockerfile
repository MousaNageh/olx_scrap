FROM python:3.11.0-alpine

RUN apk update

RUN apk add --update \
    chromium \
    chromium-chromedriver

ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
ENV GECKODRIVER_PATH=/usr/bin/geckodriver


ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt