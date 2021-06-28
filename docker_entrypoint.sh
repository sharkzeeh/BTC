#!/bin/sh

# Apply database migrations
echo "Apply database migrations"
python3 btc/manage.py migrate

# Start server
echo "Starting server"
gunicorn -b 0.0.0.0:8000 --chdir /app/btc btc.wsgi --reload -w 1