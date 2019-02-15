#!/bin/bash
set -e

python manage.py makemigrations cubane --no-input
python manage.py migrate cubane --no-input

python manage.py makemigrations media --no-input
python manage.py migrate media --no-input

python manage.py makemigrations cms --no-input
python manage.py migrate cms --no-input

python manage.py makemigrations app --no-input
python manage.py migrate app --no-input

python manage.py create_default_admin_user
python manage.py deploy

exec "$@"
