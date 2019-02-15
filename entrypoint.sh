#!/bin/bash
set -e

python manage.py makemigrations cubane --no-input
python manage.py makemigrations media --no-input
python manage.py makemigrations cms --no-input
python manage.py makemigrations backend --no-input

python manage.py makemigrations --no-input
python manage.py migrate --no-input

python manage.py create_default_admin_user

exec "$@"
