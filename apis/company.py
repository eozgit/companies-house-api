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

list_parser = reqparse.RequestParser()
list_parser.add_argument('page', type=int, location='args', default=1)
list_parser.add_argument('limit', type=int, location='args', default=10)
list_parser.add_argument('companyName', type=str, location='args')
list_parser.add_argument('region', type=str, location='args')
list_parser.add_argument('sicCode', type=int, location='args')


@api.route('')
class CompanyListApi(Resource):
    @api.marshal_list_with(company_serializer)
    def get(self):
        args = Box(list_parser.parse_args())
        query = Company.query
        if args.companyName:
            query = query.filter(
                Company.company_name.startswith(args.companyName.upper()))
        if args.region:
            region = args.region.upper()
            query = query.filter((Company.reg_address_post_town == region) | (
                Company.reg_address_county == region))
        if args.sicCode:
            query = query.filter(
                Company.sic_code_sic_text_1.startswith(str(args.sicCode)))

        return query.order_by(Company.company_number.asc()).paginate(args.page, args.limit, True, 10).items


@api.route('/<string:company_number>')
class CompanyApi(Resource):
    def get(self, company_number):
        company = Company.query.get_or_404(company_number)
        args = Box(get_parser.parse_args())
        serializer = company_serializer if not args.extend else company_with_people_serializer
        return marshal(company, serializer)

    @api.marshal_with(company_serializer)
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
    def delete(self, company_number):
        company = Company.query.get_or_404(company_number)
        db.session.delete(company)
        db.session.commit()
        return company
