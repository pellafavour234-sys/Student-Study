import sys
from pathlib import Path

import pytest


# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(BASE_DIR)
)


from backend.app import app


@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.test_client() as client:

        yield client


def test_home(client):

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "running"


def test_health(client):

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"

    assert data["model_loaded"] is True


def test_model_info(client):

    response = client.get("/model-info")

    assert response.status_code == 200

    data = response.get_json()

    assert data["model_type"] == "RandomForestRegressor"

    assert len(data["features"]) == 5


def test_prediction(client):

    student = {
        "study_hours": 6,
        "attendance": 85,
        "previous_score": 72,
        "assignments_completed": 9,
        "sleep_hours": 7
    }

    response = client.post(
        "/predict",
        json=student
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True

    assert "predicted_score" in data

    assert "performance" in data

    assert 0 <= data["predicted_score"] <= 100


def test_invalid_attendance(client):

    student = {
        "study_hours": 6,
        "attendance": 150,
        "previous_score": 72,
        "assignments_completed": 9,
        "sleep_hours": 7
    }

    response = client.post(
        "/predict",
        json=student
    )

    assert response.status_code == 400


def test_missing_field(client):

    student = {
        "study_hours": 6,
        "attendance": 85,
        "previous_score": 72,
        "assignments_completed": 9
    }

    response = client.post(
        "/predict",
        json=student
    )

    assert response.status_code == 400