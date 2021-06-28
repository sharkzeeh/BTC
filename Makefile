.PHONY: start stop build healthcheck clean install netcreate run

install:
	pip install -r requirements.txt

run:
	python btc/manage.py makemigrations
	python btc/manage.py migrate