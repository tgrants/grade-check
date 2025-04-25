#!/bin/sh
set -e

python manage.py migrate

python manage.py initadmin

gunicorn gradecheck.wsgi:application --bind 0.0.0.0:8000
