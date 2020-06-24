FROM python:3.8.3-buster

MAINTAINER "daniktarasov@gmail.com"

EXPOSE 8000

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app ./

RUN python /app/manage.py collectstatic