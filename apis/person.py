from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from box import Box
from model.orm import db
from serialize.company import person_serializer
from model.company import Company
from model.nature_of_control import NatureOfControl
from .company import api


@api.route('/<string:company_number>/person/<int:person_id>')
class PersonApi(Resource):
    @api.marshal_with(person_serializer)
    @jwt_required
    def get(self, company_number, person_id):
        company = Company.query.get_or_404(company_number)
        person = next(
            (psc for psc in company.people if psc.id == person_id), None)
        if not person:
            api.abort(404, f'Person {person_id} doesn\'t exist')
        return person

    @api.marshal_with(person_serializer)
    @jwt_required
    def put(self, company_number, person_id):
        company = Company.query.get_or_404(company_number)
        person = next(
            (psc for psc in company.people if psc.id == person_id), None)
        if not person:
            api.abort(404, f'Person {person_id} doesn\'t exist')

        payload = Box(api.payload)

        person.dob_year = payload.yearOfBirth
        person.name = payload.name
        person.nationality = payload.nationality

        for nature in person.natures_of_control:
            db.session.delete(nature)
        for nature in payload.naturesOfControl:
            noc = NatureOfControl(nature_of_control=nature.natureOfControl)
            person.natures_of_control.append(noc)

        person.notified_on = payload.notifiedOn

        db.session.commit()
        return person

    @api.marshal_with(person_serializer)
    @jwt_required
    def delete(self, company_number, person_id):
        company = Company.query.get_or_404(company_number)
        person = next(
            (psc for psc in company.people if psc.id == person_id), None)
        if not person:
            api.abort(404, f'Person {person_id} doesn\'t exist')
        db.session.delete(person)
        db.session.commit()
        return person, 204
