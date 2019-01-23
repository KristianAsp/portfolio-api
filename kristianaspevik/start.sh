#!/bin/bash

# Start gunicorn process
echo "Starting Gunicorn"
exec gunicorn kristianaspevik.wsgi:application \
    --bind 127.0.0.1:8888 \
    --workers 3
