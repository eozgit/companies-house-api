from flask_restx import Model, fields


person_serializer = Model('Person', {
    'id': fields.Integer(),
    'company_number': fields.String(),
    'address_line_1': fields.String(),
    'address_line_2': fields.String(),
    'address_care_of': fields.String(),
    'address_country': fields.String(),
    'address_locality': fields.String(),
    'address_po_box': fields.String(),
    'address_postal_code': fields.String(),
    'address_premises': fields.String(),
    'address_region': fields.String(),
    'ceased_on': fields.DateTime(),
    'country_of_residence': fields.String(),
    'dob_day': fields.Integer(),
    'dob_month': fields.Integer(),
    'dob_year': fields.Integer(),
    'etag': fields.String(),
    'id_country_registered': fields.String(),
    'id_legal_authority': fields.String(),
    'id_legal_form': fields.String(),
    'id_place_registered': fields.String(),
    'id_registration_number': fields.String(),
    'kind': fields.String(),
    'link_self': fields.String(),
    'link_statement': fields.String(),
    'name': fields.String(),
    'forename': fields.String(),
    'other_forenames': fields.String(),
    'surname': fields.String(),
    'title': fields.String(),
    'nationality': fields.String(),
    # 'natures_of_control': fields.List(fields.Nested(natures_of_control_serializer))
    'notified_on': fields.DateTime()
})
