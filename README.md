# FastAPI CoinGecko

A FastAPI web application that fetches and displays cryptocurrency exchange rates from the CoinGecko API.

This project is containerized with Docker, tested with Pytest, and deployed to GHCR (GitHub Container Registry) using GitHub Actions with Helm chart support.

## Features

- 🚀 FastAPI application serving real-time cryptocurrency data from CoinGecko
- 🎨 HTML templating with Jinja2
- 🐳 Dockerized for easy deployment
- ☸️ Helm chart for Kubernetes deployment (minikube compatible)
- 🔄 CI/CD pipeline using GitHub Actions
- 💚 Health checks with readiness and liveness probes
- ✅ Comprehensive unit tests with pytest
- 🔒 Container vulnerability scanning with Trivy

## Quick Start

### Local Development

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   Access at [http://localhost:8000](http://localhost:8000)

### Docker

1. **Build the image**
   ```bash
   docker build -t infra-coingecko .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 infra-coingecko
   ```

### Testing

Run tests with coverage report:
```bash
pytest --cov=app --cov-report term-missing -v
```

## Deployment

### Helm Charts

Access the Helm chart repository:
- Repository index: https://shabz3.github.io/infra-coingecko/index.yaml
- Releases: https://github.com/shabz3/infra-coingecko/releases

### Container Registry

Pre-built Docker images are available at:
https://github.com/shabz3/infra-coingecko/pkgs/container/infra-coingecko

## Run in Minikube using helm

Assumes minkube is installed and started with `minkube start`

1. Install with
```bash
helm install coingecko charts/infra-coingecko
```

2. Check pods are working with
```bash
kubectl get pod
```

3. Get the name of the service with
```bash
kubectl get svc
```

4. Port forward the service with
```bash
kubectl service coingecko-service
```

5. Go to the URL printed (IP of your service)