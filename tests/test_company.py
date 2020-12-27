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
        headers = {'Authentication': f'Bearer {data.access_token}'}
        yield (client, headers)


def test_company_list(auth):
    client, headers = auth
    response = client.get(
        '/company', headers=headers)
    companies = response.get_json()
    assert isinstance(companies, list)
    company = companies[0]
    assert 'companyName' in company
    assert 'companyNumber' in company
    assert 'incorporationDate' in company
