#!/bin/bash

## use uwsgi

## use gunicorn

log_directory=`pwd`/log
log_path=$log_directory/sso.log

hash gunicorn 2>&- || { echo >&2 "I require gunicorn but it's not installed.  Aborting."; exit 1; }


echo "ps aux | grep gunico | grep sso  | awk '{print $2}' | xargs kill -HUP"
ps aux | grep gunico | grep sso | awk '{print $2}' | xargs kill -HUP

mkdir -p $log_directory

echo "gunicorn -c gunicorn.conf sso:app -D -t 6000 --error-logfile $log_path --log-level info"
gunicorn -c gunicorn.conf sso:app -D -t 6000 --error-logfile $log_path --log-level info

echo "ps aux | grep  gunicor"
sleep 2;
ps aux | grep  gunicor
