from flask_restx import Model, fields


person_serializer = Model('Person', {
    'name': fields.String(),
    'nationality': fields.String()
})
