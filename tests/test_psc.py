import pytest
from box import Box
from app import app
from model.orm import db


@pytest.fixture
def auth():
    with app.test_client() as client:
        response = client.post(
            '/token', json={'username': 'test', 'password': 'test'})
        data = response.get_json()
        data = Box(data)
        headers = {'Authorization': f'Bearer {data.access_token}'}
        yield (client, headers)


def test_psc_search(auth):
    client, headers = auth
    response = client.get(
        '/company/10919507/person?nationality=Spanish&yearOfBirth=1977', headers=headers)
    people = response.get_json()
    assert isinstance(people, list)
    person = Box(people[0])
    assert person.name == 'Mr. Alejandro Ruiz Rodriguez'
