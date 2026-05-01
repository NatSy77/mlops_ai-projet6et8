from fastapi.testclient import TestClient

from app.main import app
from app.predict import encoded_columns

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_endpoint_returns_prediction():
    payload = {
        "features": [0.0] * len(encoded_columns)
    }

    response = client.post("/predict", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert "probability" in data
    assert "prediction" in data
    assert "decision" in data
    assert "threshold" in data
    assert data["decision"] in ["accepted", "refused"]