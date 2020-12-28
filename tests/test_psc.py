from box import Box
from fixture_authorization import auth
from model.orm import db


def test_psc_search(auth):
    client, headers = auth
    response = client.get(
        '/company/10919507/person?nationality=Spanish&yearOfBirth=1977', headers=headers)
    people = response.get_json()
    assert isinstance(people, list)
    person = Box(people[0])
    assert person.name == 'Mr. Alejandro Ruiz Rodriguez'
