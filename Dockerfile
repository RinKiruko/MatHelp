FROM python:3.8.3-buster

MAINTAINER "daniktarasov@gmail.com"

EXPOSE 8000

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./app /app

RUN python /app/manage.py collectstatic
