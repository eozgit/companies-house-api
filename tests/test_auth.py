import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_login_with_valid_credentials(client):
    response = client.post(
        '/token', json={'username': 'test', 'password': 'test'})
    data = response.get_json()
    assert 'access_token' in data


def test_login_with_invalid_credentials(client):
    response = client.post(
        '/token', json={'username': 'test', 'password': 'testx'})
    data = response.get_json()
    assert 'access_token' not in data
