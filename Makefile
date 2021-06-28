.PHONY: start stop build healthcheck clean install netcreate run

# healthcheck: healthchecker.sh
# 	./healthchecker.sh

# netcreate:
# 	docker network create net || true

install:
	pip install --upgrade pip
	pip install -r requirements.txt

build: Dockerfile
	docker-compose build

start: build
	docker-compose up -d

stop:
	docker-compose down
