# Makefile

.PHONY: install run test docker-build docker-run deploy

install:
	pip install -r requirements.txt

run:
	python src/main.py

test:
	pytest tests/

docker-build:
	docker build -t healthcheck-api .

docker-run:
	docker run -p 8000:8000 healthcheck-api

deploy:
	kubectl apply -f deploy/k8s/deployment.yaml
	kubectl apply -f deploy/k8s/service.yaml