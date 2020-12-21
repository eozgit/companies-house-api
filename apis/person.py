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
        