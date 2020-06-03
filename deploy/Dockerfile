FROM python:3.6

WORKDIR /app

COPY ./deploy/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./src /app

CMD uwsgi --wsgi-file /app/urlshortener/wsgi.py --http 0.0.0.0:8000
