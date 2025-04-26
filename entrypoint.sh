#!/bin/sh
set -e

python manage.py migrate

python manage.py initadmin

if [ "$DJANGO_DEBUG" = "True" ]; then
	python manage.py runserver 0.0.0.0:8000
else
	python manage.py collectstatic --noinput
	gunicorn gradecheck.wsgi:application --bind 0.0.0.0:8000
fi
