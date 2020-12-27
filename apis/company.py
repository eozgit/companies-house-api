from flask_restx import Namespace, Resource, reqparse, marshal
from flask_jwt_extended import jwt_required
from box import Box
from model.orm import db
from serialize.company import company_serializer, company_with_people_serializer
from model.company import Company


api = Namespace('company')


get_parser = reqparse.RequestParser()
get_parser.add_argument(
    'extend', type=bool, location='args', default=False)


@api.route('/<string:company_number>')
class CompanyApi(Resource):
    @jwt_required
    def get(self, company_number):
        company = Company.query.get_or_404(company_number)
        args = Box(get_parser.parse_args())
        serializer = company_serializer if not args.extend else company_with_people_serializer
        return marshal(company, serializer)

    @api.marshal_with(company_serializer)
    @jwt_required
    def put(self, company_number):
        company = Company.query.get_or_404(company_number)

        payload = Box(api.payload)
        company.company_name = payload.companyName
        company.reg_address_address_line1 = payload.addressLine1
        company.reg_address_address_line2 = payload.addressLine2
        company.reg_address_post_town = payload.addressPostTown
        company.reg_address_county = payload.addressCounty
        company.reg_address_country = payload.addressCountry
        company.reg_address_post_code = payload.addressPostCode
        company.company_category = payload.companyCategory
        company.company_status = payload.companyStatus
        company.country_of_origin = payload.countryOfOrigin
        company.sic_code_sic_text_1 = payload.sicCode
        company.uri = payload.uri
        db.session.commit()
        return company

    @api.marshal_with(company_serializer)
    @jwt_required
    def delete(self, company_number):
        company = Company.query.get_or_404(company_number)
        db.session.delete(company)
        db.session.commit()
        return company, 204
