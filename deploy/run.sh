#!/usr/bin/env bash

/app/manage.py migrate --noinput
/app/manage.py collectstatic --noinput

uwsgi --wsgi-file /app/urlshortener/wsgi.py --socket /app/sock/uwsgi.sock --chmod-socket=666