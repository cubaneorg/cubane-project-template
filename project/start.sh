#!/bin/bash
gunicorn -w 4 app.wsgi:application -b 127.0.0.1:8080 --daemon
nginx -g 'daemon off;'
