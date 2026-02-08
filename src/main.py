from fastapi import FastAPI
import logging
from src.api.health import router as health_router

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("healthcheck-app")

app = FastAPI()

@app.on_event("startup")
def on_startup():
    logger.info("APP STARTUP: Health Check API starting")

@app.on_event("shutdown")
def on_shutdown():
    logger.info("APP SHUTDOWN: Health Check API shutting down")

app.include_router(health_router)