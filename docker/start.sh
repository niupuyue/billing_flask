#!/bin/sh
rm -rf migrations
flask db init && flask db migrate && flask db upgrade && flask admin init
exec gunicorn -c gunicorn.conf.py "billing-flask:create_app()"