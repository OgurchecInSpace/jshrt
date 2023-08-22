#!/bin/sh
source venv/bin/activate
flask db upgrade
exec python -u jshrt.py
#exec gunicorn -b :8080 --access-logfile - --error-logfile - jshrt:app