# Health Check API

Simple Health Check API built with FastAPI. Useful as a minimal example for local development, testing, Docker, and basic Kubernetes deployment.

## Project layout (important files)
- src/main.py               — FastAPI app, startup/shutdown logs, router registration
- src/api/health.py         — /health route, entry/exit logs
- src/services/health_service.py — HealthService implementation
- tests/test_health.py      — unit test for /health
- Dockerfile                — image build
- deploy/k8s/*              — minimal k8s manifests
- requirements.txt          — Python deps
- Makefile                  — helper targets

## Prerequisites
- Python 3.10+
- pip
- (optional) Docker
- (optional) kubectl and a Kubernetes cluster

Tested on macOS — commands below assume a Mac terminal.

## Quick start (local)
1. From project root:
   ```
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run dev server:
   ```
   uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. Hit the endpoint:
   ```
   curl http://127.0.0.1:8000/health
   ```
   Example response:
   ```
   {"status":"ok","checks":{"database":{"database":"healthy"},"service":{"service":"available"}}}
   ```

## Logging
- Startup/shutdown logs printed by src/main.py:
  - "APP STARTUP: Health Check API starting"
  - "APP SHUTDOWN: Health Check API shutting down"
- Request-level entry/exit logs from src/api/health.py:
  - ENTRY: /health - method=GET client=...
  - EXIT: /health - status=200 checks_keys=[...]

Check the terminal running uvicorn to see these logs.

## Tests
Run unit tests with:
```
pytest -q
```

There is a FastAPI TestClient test at tests/test_health.py that verifies the /health JSON.

## Docker
Build and run:
```
docker build -t healthcheck-api .
docker run -p 8000:8000 healthcheck-api
```
Or use Makefile:
```
make docker-build
make docker-run
```

## Kubernetes (minimal)
Ensure image `healthcheck-api:latest` is available to the cluster (push to registry or use local kind/docker-desktop image load). Apply manifests:
```
kubectl apply -f deploy/k8s/deployment.yaml
kubectl apply -f deploy/k8s/service.yaml
```

## Extending health checks
- Replace stub methods in src/services/health_service.py with real probes (DB, Redis, external APIs).
- Consider async checks for IO-bound probes and set proper timeouts.
- Return suitable HTTP status codes (e.g., 500) for degraded/unhealthy states if desired.

## Troubleshooting
- "ImportError" or circular import: ensure src/__init__.py exists and main.py imports the router only (app.include_router).
- If uvicorn doesn't pick up changes, confirm you're running `uvicorn src.main:app --reload`.
- For permission or port issues on mac, try a different port or run with sudo only if necessary.

## Contributing
Fork → branch → PR. Keep changes small and add tests for functionality.

## License
MIT
