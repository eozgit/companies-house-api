from flask_restx import Namespace, Resource
from flask_jwt_extended import create_access_token
from box import Box


api = Namespace('token')


@api.route('')
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
