from flask_restx import Api
from .token import api as token
from .company import api as company


api = Api()


api.add_namespace(token)
api.add_namespace(company)
