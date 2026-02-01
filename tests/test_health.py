from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    json = response.json()
    assert isinstance(json.get("status"), int)
    assert json["status"] == 200
    assert "checks" in json