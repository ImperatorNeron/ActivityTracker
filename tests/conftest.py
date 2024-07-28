import pytest
from starlette.testclient import TestClient

from src.main import application


@pytest.fixture
def client():
    with TestClient(app=application) as client:
        yield client


@pytest.fixture
def auth_headers_for_user(client):
    login_data = {
        "username": "vlad@example.com",
        "password": "1",
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = client.post(
        url="/api/v1/auth/login",
        data=login_data,
        headers=headers,
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
