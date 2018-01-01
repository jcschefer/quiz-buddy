#!/bin/bash

cd web
python manage.py collectstatic
gunicorn web.wsgi --log-file -
