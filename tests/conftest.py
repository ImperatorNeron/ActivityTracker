import pytest
from starlette.testclient import TestClient

from src.main import application


@pytest.fixture
def client():
    with TestClient(app=application) as client:
        yield client


def get_user_token(client, login_data):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = client.post(
        url="/api/v1/auth/login",
        data=login_data,
        headers=headers,
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def auth_headers_for_user(client):
    login_data = {
        "username": "vlad@example.com",
        "password": "1",
    }
    return get_user_token(client, login_data)


@pytest.fixture
def auth_headers_for_user_2(client):
    login_data = {
        "username": "user@user.com",
        "password": "1",
    }
    return get_user_token(client, login_data)
