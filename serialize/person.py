from flask_restx import Model, fields
from .nature_of_control import nature_of_control_serializer


person_serializer = Model('Person', {
    'id': fields.Integer(attribute='id'),
    'yearOfBirth': fields.Integer(attribute='dob_year'),
    'name': fields.String(attribute='name'),
    'nationality': fields.String(attribute='nationality'),
    'naturesOfControl': fields.List(fields.Nested(nature_of_control_serializer), attribute='natures_of_control'),
    'notifiedOn': fields.Date(attribute='notified_on')
})
