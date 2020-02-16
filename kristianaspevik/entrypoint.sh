#!/usr/bin/env bash

# Prepare log files and start outputting logs to stdout
touch /var/log/kristianaspevik/gunicorn.log
touch /var/log/kristianaspevik/gunicorn-access.log

export DJANGO_SETTINGS_MODULE=kristianaspevik.settings
#python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate

# Copy static files to shared volume
#cp -R static/* /opt/static/

exec gunicorn kristianaspevik.wsgi:application \
    --name projectx_django \
    --bind 0.0.0.0:8000 \
    --workers 5 \
    --log-level=info \
    --log-file=/var/log/kristianaspevik/gunicorn.log \
    --access-logfile=/var/log/kristianaspevik/gunicorn-access.log \
"$@"
