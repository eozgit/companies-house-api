from flask_restx import Model, fields
from .nature_of_control import nature_of_control_serializer


person_serializer = Model('Person', {
    'id': fields.Integer(attribute='id'),
    'addressLine1': fields.String(attribute='address_line_1'),
    'addressLine2': fields.String(attribute='address_line_2'),
    'addressCareOf': fields.String(attribute='address_care_of'),
    'addressCountry': fields.String(attribute='address_country'),
    'addressLocality': fields.String(attribute='address_locality'),
    'addressPoBox': fields.String(attribute='address_po_box'),
    'addressPostalCode': fields.String(attribute='address_postal_code'),
    'addressPremises': fields.String(attribute='address_premises'),
    'addressRegion': fields.String(attribute='address_region'),
    'ceasedOn': fields.DateTime(attribute='ceased_on'),
    'countryOfResidence': fields.String(attribute='country_of_residence'),
    'dobDay': fields.Integer(attribute='dob_day'),
    'dobMonth': fields.Integer(attribute='dob_month'),
    'dobYear': fields.Integer(attribute='dob_year'),
    'etag': fields.String(attribute='etag'),
    'idCountryRegistered': fields.String(attribute='id_country_registered'),
    'idLegalAuthority': fields.String(attribute='id_legal_authority'),
    'idLegalForm': fields.String(attribute='id_legal_form'),
    'idPlaceRegistered': fields.String(attribute='id_place_registered'),
    'idRegistrationNumber': fields.String(attribute='id_registration_number'),
    'kind': fields.String(attribute='kind'),
    'linkSelf': fields.String(attribute='link_self'),
    'linkStatement': fields.String(attribute='link_statement'),
    'name': fields.String(attribute='name'),
    'forename': fields.String(attribute='forename'),
    'otherForenames': fields.String(attribute='other_forenames'),
    'surname': fields.String(attribute='surname'),
    'title': fields.String(attribute='title'),
    'nationality': fields.String(attribute='nationality'),
    'naturesOfControl': fields.List(fields.Nested(nature_of_control_serializer), attribute='natures_of_control'),
    'notifiedOn': fields.DateTime(attribute='notified_on')
})
