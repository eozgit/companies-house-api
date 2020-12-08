from flask import Flask
from flask_restx import Resource, Api
from model.orm import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
api = Api(app)


@api.route('/house')
class House(Resource):
    def get(self):
        return {'house': 'companies'}


if __name__ == '__main__':
    app.run(debug=True)
