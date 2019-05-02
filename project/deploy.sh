#!/bin/bash
python manage.py makemigrations
python manage.py migrate

python manage.py country_fixture
python manage.py create_default_admin_user

python manage.py deploy

find . -name '*.pyc' -delete
