#!/bin/sh 
until timeout 10s celery -A tasks inspect ping; do
  >&2 echo "Celery workers not available"
done
echo 'Starting flower'
celery -A tasks flower