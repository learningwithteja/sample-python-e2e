# Contents of /healthcheck-api/healthcheck-api/src/core/config.py

import os

class Config:
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./test.db')
    SERVICE_NAME = os.getenv('SERVICE_NAME', 'HealthCheckAPI')
    VERSION = os.getenv('VERSION', '1.0.0')