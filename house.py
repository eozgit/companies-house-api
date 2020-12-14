from flask import Flask
from flask_restx import Api, Resource
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from box import Box
from model.orm import db
from model.company import Company
from serialize.company import company


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'


db.init_app(app)
api = Api(app)
jwt = JWTManager(app)


api.models[company.name] = company


@api.route('/login')
class Login(Resource):
    def post(self):
        payload = Box(api.payload)
        username = payload.username
        password = payload.password

        if not username:
            return {'message': 'Missing username parameter'}, 400
        if not password:
            return {'message': 'Missing password parameter'}, 400

        if username != 'test' or password != 'test':
            return {'message': 'Bad username or password'}, 401

        access_token = create_access_token(identity=username)
        return {'access_token': access_token}, 200


@api.route('/company/<string:id>')
class CompanyApi(Resource):
    @api.marshal_with(company)
    def get(self, id):
        return Company.query.get_or_404(id)

    @api.marshal_with(company)
    def put(self, id):
        company = Company.query.get_or_404(id)

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

    @api.marshal_with(company)
    def delete(self, id):
        company = Company.query.get_or_404(id)
        db.session.delete(company)
        db.session.commit()
        return company


if __name__ == '__main__':
    app.run(debug=True)
