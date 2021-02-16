#!/bin/sh
gunicorn -w 1 -b 0:8000 btc.wsgi:application