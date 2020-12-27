import datetime
from flask_restx import Resource, reqparse
from flask_jwt_extended import jwt_required
from box import Box
from model.orm import db
from serialize.person import person_serializer
from model.company import Company
from model.person import Person
from model.nature_of_control import NatureOfControl
from .company import api


psc_list_parser = reqparse.RequestParser()
psc_list_parser.add_argument('name', type=str, location='args')
psc_list_parser.add_argument('yearOfBirth', type=int, location='args')
psc_list_parser.add_argument('nationality', type=str, location='args')


@api.route('/<string:company_number>/person')
class PersonListApi(Resource):
    @api.marshal_list_with(person_serializer)
    @jwt_required
    def get(self, company_number):
        args = Box(psc_list_parser.parse_args())
        company = Company.query.get_or_404(company_number)
        people = company.people
        return [person for person in people if
                (not args.name or args.name.lower() in person.name.lower()) and
                (not args.yearOfBirth or person.dob_year == args.yearOfBirth) and
                (not args.nationality or person.nationality.lower() == args.nationality.lower())]

    @api.marshal_with(person_serializer)
    @jwt_required
    def post(self, company_number):
        company = Company.query.get_or_404(company_number)
        payload = Box(api.payload)

        person = Person(
            name=payload.name,
            nationality=payload.nationality,
            dob_year=payload.yearOfBirth,
            notified_on=payload.notifiedOn,
            natures_of_control=[],

            address_line_1='',
            address_line_2='',
            address_care_of='',
            address_country='',
            address_locality='',
            address_po_box='',
            address_postal_code='',
            address_premises='',
            address_region='',
            ceased_on=db.func.now(),
            country_of_residence='',
            dob_day=0,
            dob_month=0,
            etag='',
            id_country_registered='',
            id_legal_authority='',
            id_legal_form='',
            id_place_registered='',
            id_registration_number='',
            kind='',
            link_self='',
            link_statement='',
            forename='',
            other_forenames='',
            surname='',
            title=''
        )
        for nature in payload.naturesOfControl:
            noc = NatureOfControl(nature_of_control=nature.natureOfControl)
            person.natures_of_control.append(noc)

        company.people.append(person)
        db.session.commit()
        return person, 201
