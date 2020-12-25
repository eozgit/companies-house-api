from flask import Flask
from flask_jwt_extended import JWTManager
from model.orm import db
from apis import api
from serialize.company import company_serializer, company_with_people_serializer
from serialize.person import person_serializer
from serialize.nature_of_control import nature_of_control_serializer


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'


for model in [company_serializer, company_with_people_serializer, person_serializer, nature_of_control_serializer]:
    api.models[model.name] = model


db.init_app(app)
jwt = JWTManager(app)
api.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
