import pytest
from box import Box
from app import app


@pytest.fixture
def auth():
    with app.test_client() as client:
        response = client.post(
            '/token', json={'username': 'test', 'password': 'test'})
        data = response.get_json()
        data = Box(data)
        headers = {'Authorization': f'Bearer {data.access_token}'}
        yield (client, headers)
