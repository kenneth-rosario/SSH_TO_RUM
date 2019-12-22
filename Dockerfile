FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libressl-dev libffi-dev \
    libc-dev nodejs yarn make

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /src

WORKDIR /src

COPY src /src
