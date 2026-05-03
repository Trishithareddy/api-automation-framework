import pytest
from utils.api_client import APIClient
from payloads.user_payload import create_user_payload
from utils.logger import get_logger


client = APIClient()
logger = get_logger()


def test_get_users():
    logger.info("Testing GET users API")

    response = client.get("/users")

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert "name" in response.json()[0]
    assert "email" in response.json()[0]


@pytest.mark.parametrize("name, job", [
    ("Test User", "QA Engineer"),
    ("Automation Tester", "SDET"),
    ("API Tester", "Quality Analyst")
])
def test_create_user_data_driven(name, job):
    logger.info(f"Testing POST user API with name={name}, job={job}")

    payload = {
        "name": name,
        "job": job
    }

    response = client.post("/users", payload)

    assert response.status_code == 201
    assert response.json()["name"] == name
    assert response.json()["job"] == job


def test_update_user():
    logger.info("Testing PUT user API")

    payload = {
        "name": "Updated User",
        "job": "Senior QA"
    }

    response = client.put("/users/1", payload)

    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"
    assert response.json()["job"] == "Senior QA"


def test_delete_user():
    logger.info("Testing DELETE user API")

    response = client.delete("/users/1")

    assert response.status_code == 200
