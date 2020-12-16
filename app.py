from flask import Flask
from flask_jwt_extended import JWTManager
from model.orm import db
from apis import api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'


db.init_app(app)
jwt = JWTManager(app)
api.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
