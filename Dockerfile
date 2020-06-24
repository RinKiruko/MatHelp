FROM heroku/heroku:18

MAINTAINER "daniktarasov@gmail.com"

EXPOSE 8000

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app ./

RUN python /app/manage.py collectstatic

CMD gunicorn --workers=3 --bind 0.0.0.0:$PORT config.wsgi
