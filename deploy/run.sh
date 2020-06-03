#!/usr/bin/env bash

/app/manage.py migrate --noinput
/app/manage.py collectstatic --noinput

uwsgi --wsgi-file /app/urlshortener/wsgi.py --http 0.0.0.0:8000