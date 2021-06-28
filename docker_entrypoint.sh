#!/bin/sh

# Apply database migrations
echo "Apply database migrations"
python3 btc/manage.py migrate

# Start server
echo "Starting server"
python3 btc/manage.py runserver 0.0.0.0:8000