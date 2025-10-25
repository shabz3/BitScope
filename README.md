# FastAPI CoinGecko

A FastAPI web app that fetches and displays cryptocurrency exchange rates from the CoinGecko API.

This project is containerized with Docker, tested with Pytest and helm chart (and Docker image) published to GHCR using GitHub Actions.

## Features
- FastAPI app serving data from CoinGecko

- HTML templating with Jinja2

- Dockerized for easy deployment

- Helm chart for Kubernetes (minikube compatible)

- CI/CD using GitHub Actions

- Includes readiness and liveness probes for production resilience

- Unit tests via pytest

## Run Locally
### Install dependencies
`pip install -r requirements.txt`

### Run App
`uvicorn app.main:app --host 0.0.0.0 --port 8000`
(http://localhost:8000/)

## Image Build & Run
`docker build -t infra-coingecko .`

### Run
`docker run -p 8000:8000 infra-coingecko`

## Run tests
`pytest --cov=app --cov-report term-missing -v`

## Access Helm charts:
https://shabz3.github.io/infra-coingecko/index.yaml
Or go to https://github.com/shabz3/infra-coingecko/releases

## Access container registry
https://github.com/shabz3/infra-coingecko/pkgs/container/infra-coingecko
