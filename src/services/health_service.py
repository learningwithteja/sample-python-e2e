class HealthService:
    def check_database(self):
        # Logic to check database connectivity
        return {"database": "healthy"}

    def check_service_availability(self):
        # Logic to check other service availability
        return {"service": "available"}

    def perform_health_check(self):
        health_status = {
            "database": self.check_database(),
            "service": self.check_service_availability(),
        }
        return health_status