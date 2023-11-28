#!/bin/bash 

echo " Create Migration"
python manage.py makemigrations UsersApp

echo "Migrate"
python manage.py migrate --no-input

echo "Start Server"
python manage.py runserver 0.0.0.0:8000