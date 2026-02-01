from fastapi import APIRouter, Request
import logging
from src.services.health_service import HealthService

router = APIRouter()
logger = logging.getLogger("healthcheck-app")

@router.get("/health")
def health_check(request: Request):
    logger.info(f"ENTRY: /health - method={request.method} client={request.client.host}")
    svc = HealthService()
    try:
        checks = svc.perform_health_check()
        response = {"status": 200, "checks": checks}  # numeric status
        logger.info(f"EXIT: /health - status=200 checks_keys={list(checks.keys())}")
        return response
    except Exception:
        logger.exception("ERROR in /health")
        raise