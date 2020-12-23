from flask_restx import Model, fields


nature_of_control_serializer = Model('NatureOfControl', {
    'natureOfControl': fields.String(attribute='nature_of_control')
})
