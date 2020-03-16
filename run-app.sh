#!/bin/sh

WORKERS_NUM=${1:-1}
PORT=${2:-8000}

# see https://github.com/encode/uvicorn/issues/589
export FORWARDED_ALLOW_IPS="*"

exec 2>&1 gunicorn \
  ppm_telegram_bot.api:app \
  --forwarded-allow-ips="*" \
  --workers=$WORKERS_NUM \
  --worker-class=uvicorn.workers.UvicornWorker \
  --bind=0.0.0.0:$PORT
