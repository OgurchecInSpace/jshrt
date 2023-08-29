#!/bin/sh
source venv/bin/activate
flask db upgrade
exec python jshrt.py
