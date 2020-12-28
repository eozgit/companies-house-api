from box import Box
from fixture_authorization import auth
from app import app
from model.orm import db
from model.person import Person


def test_psc_search(auth):
    client, headers = auth
    response = client.get(
        '/company/10919507/person?nationality=Spanish&yearOfBirth=1977', headers=headers)
    people = response.get_json()
    assert isinstance(people, list)
    person = Box(people[0])
    assert person.name == 'Mr. Alejandro Ruiz Rodriguez'


def test_psc_create(auth):
    with app.app_context():
        test_data = Person.query.filter(
            Person.name == 'Jane Doe').all()
        for p in test_data:
            db.session.delete(p)
        db.session.commit()

    client, headers = auth
    response = client.post(
        '/company/10919507/person', headers=headers, json={
            'yearOfBirth': 1980,
            'name': 'Jane Doe',
            'nationality': 'Kenyan',
            'naturesOfControl': [
                {
                    'natureOfControl': 'ownership-of-shares-75-to-100-percent'
                },
                {
                    'natureOfControl': 'voting-rights-75-to-100-percent'
                },
                {
                    'natureOfControl': 'right-to-appoint-and-remove-directors'
                }
            ],
            'notifiedOn': '2020-12-28'
        })
    person = response.get_json()
    person = Box(person)
    assert person.name == 'Jane Doe'
    assert person.yearOfBirth == 1980
