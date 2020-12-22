from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from box import Box
from model.orm import db
from serialize.company import person_serializer
from model.company import Company
from .company import api


@api.route('/<string:company_number>/person/<int:person_id>')
class PersonApi(Resource):
    @api.marshal_with(person_serializer)
    def get(self, company_number, person_id):
        company = Company.query.get_or_404(company_number)
        person = next(
            (psc for psc in company.people if psc.id == person_id), None)
        if not person:
            api.abort(404, f'Person {person_id} doesn\'t exist')
        return person

    @api.marshal_with(person_serializer)
    def put(self, company_number, person_id):
        company = Company.query.get_or_404(company_number)
        person = next(
            (psc for psc in company.people if psc.id == person_id), None)
        if not person:
            api.abort(404, f'Person {person_id} doesn\'t exist')

        payload = Box(api.payload)

        person.address_line_1 = payload.address_line_1
        person.address_line_2 = payload.address_line_2
        person.address_care_of = payload.address_care_of
        person.address_country = payload.address_country
        person.address_locality = payload.address_locality
        person.address_po_box = payload.address_po_box
        person.address_postal_code = payload.address_postal_code
        person.address_premises = payload.address_premises
        person.address_region = payload.address_region
        person.ceased_on = payload.ceased_on
        person.country_of_residence = payload.country_of_residence
        person.dob_day = payload.dob_day
        person.dob_month = payload.dob_month
        person.dob_year = payload.dob_year
        person.id_country_registered = payload.id_country_registered
        person.id_legal_authority = payload.id_legal_authority
        person.id_legal_form = payload.id_legal_form
        person.id_place_registered = payload.id_place_registered
        person.id_registration_number = payload.id_registration_number
        person.kind = payload.kind
        person.link_self = payload.link_self
        person.link_statement = payload.link_statement
        person.name = payload.name
        person.forename = payload.forename
        person.other_forenames = payload.other_forenames
        person.surname = payload.surname
        person.title = payload.title
        person.nationality = payload.nationality
        # person.natures_of_control = payload.natures_of_control
        person.notified_on = payload.notified_on

        db.session.commit()
        return person

    @api.marshal_with(person_serializer)
    def delete(self, company_number, person_id):
        company = Company.query.get_or_404(company_number)
        person = next(
            (psc for psc in company.people if psc.id == person_id), None)
        if not person:
            api.abort(404, f'Person {person_id} doesn\'t exist')
        db.session.delete(person)
        db.session.commit()
        return person, 204
