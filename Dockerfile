FROM python:3.8.3-buster

MAINTAINER "daniktarasov@gmail.com"

EXPOSE 8000

RUN ls -l

COPY ./ /app

RUN pip install -r requirements.txt

RUN python /app/manage.py collectstatic
