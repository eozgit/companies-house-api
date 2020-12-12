from flask import Flask
from flask_restx import Api, Resource
from box import Box
from model.orm import db
from model.company import Company
from serialize.company import company

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
api = Api(app)


api.models[company.name] = company


@api.route('/house')
class House(Resource):
    def get(self):
        return {'house': 'companies'}


@api.route('/company/<string:id>')
class CompanyApi(Resource):
    @api.marshal_with(company)
    def get(self, id):
        return Company.query.get_or_404(id)

    @api.marshal_with(company)
    def put(self, id):
        payload = Box(api.payload)
        company = Company.query.get(id)
        company.company_name = payload.company_name
        company.reg_address_address_line1 = payload.reg_address_address_line1
        company.reg_address_address_line2 = payload.reg_address_address_line2
        company.reg_address_post_town = payload.reg_address_post_town
        company.reg_address_county = payload.reg_address_county
        company.reg_address_country = payload.reg_address_country
        company.reg_address_post_code = payload.reg_address_post_code
        company.company_category = payload.company_category
        company.company_status = payload.company_status
        company.country_of_origin = payload.country_of_origin
        company.sic_code_sic_text_1 = payload.sic_code_sic_text_1
        company.uri = payload.uri
        db.session.commit()
        return company


if __name__ == '__main__':
    app.run(debug=True)
