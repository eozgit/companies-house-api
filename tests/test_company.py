from box import Box
from fixture_authorization import auth
from app import app
from model.orm import db
from model.company import Company


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


def test_company_search(auth):
    client, headers = auth
    response = client.get(
        '/company?companyName=LIGHTHOUSE&region=STAFFORDSHIRE&sicCode=47910', headers=headers)
    companies = response.get_json()
    assert isinstance(companies, list)
    company = Box(companies[0])
    assert company.companyName == 'LIGHTHOUSELIGHT LTD'


def test_company_create(auth):
    with app.app_context():
        test_data = Company.query.filter(
            Company.company_name == 'TEST COMPANY LTD').all()
        for c in test_data:
            db.session.delete(c)
        db.session.commit()

    client, headers = auth
    response = client.post(
        '/company', headers=headers, json={
            'companyName': 'TEST COMPANY LTD',
            'addressLine1': 'Test address',
            'addressLine2': '',
            'addressPostTown': 'Test Town',
            'addressCounty': 'City of London',
            'addressCountry': 'ENGLAND',
            'addressPostCode': 'E1 6AN',
            'companyCategory': 'Private Limited Company',
            'companyStatus': 'Active',
            'countryOfOrigin': 'United Kingdom',
            'incorporationDate': '27/12/2020',
            'sicCode': '62012 - Business and domestic software development',
            'uri': 'http://business.data.gov.uk/id/company/TBD'
        })
    company = response.get_json()
    company = Box(company)
    assert company.companyName == 'TEST COMPANY LTD'
    assert 'companyNumber' in company


def test_company_update(auth):
    with app.app_context():
        record = Company.query.filter(
            Company.company_name == 'TEST COMPANY LTD').first()

    client, headers = auth
    response = client.put(
        f'/company/{record.company_number}', headers=headers, json={
            'companyName': 'TEST COMPANY LTD',
            'addressLine1': 'Test address',
            'addressLine2': '',
            'addressPostTown': 'Test Town',
            'addressCounty': 'City of London',
            'addressCountry': 'ENGLAND',
            'addressPostCode': 'E1 6AN',
            'companyCategory': 'Private Limited Company',
            'companyStatus': 'Active',
            'countryOfOrigin': 'United Kingdom',
            'incorporationDate': '27/12/2020',
            'sicCode': '62012 - Business and domestic software development',
            'uri': f'http://business.data.gov.uk/id/company/{record.company_number}'
        })
    company = response.get_json()
    company = Box(company)
    assert company.uri.endswith(record.company_number)


def test_company_read(auth):
    with app.app_context():
        record = Company.query.filter(
            Company.company_name == 'TEST COMPANY LTD').first()

    client, headers = auth
    response = client.get(
        f'/company/{record.company_number}', headers=headers)
    company = response.get_json()
    company = Box(company)
    assert company.companyNumber == record.company_number
    assert company.companyName == record.company_name


def test_company_delete(auth):
    with app.app_context():
        record = Company.query.filter(
            Company.company_name == 'TEST COMPANY LTD').first()

    client, headers = auth
    response = client.delete(
        f'/company/{record.company_number}', headers=headers)

    with app.app_context():
        record = Company.query.filter(
            Company.company_number == record.company_number).first()

    assert record is None
