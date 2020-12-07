from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_number = db.Column(db.String(50))

    # "address": {
    #     "address_line_1": "string",
    #     "address_line_2": "string",
    #     "care_of": "string",
    #     "country": "string",
    #     "locality": "string",
    #     "po_box": "string",
    #     "postal_code": "string",
    #     "premises": "string",
    #     "region": "string"
    # },

    address_line_1 = db.Column(db.String(500))
    address_line_2 = db.Column(db.String(500))
    address_care_of = db.Column(db.String(500))
    address_country = db.Column(db.String(500))
    address_locality = db.Column(db.String(500))
    address_po_box = db.Column(db.String(500))
    address_postal_code = db.Column(db.String(500))
    address_premises = db.Column(db.String(500))
    address_region = db.Column(db.String(500))

    # "ceased_on": "date",
    # "country_of_residence": "string", nullable

    ceased_on = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)
    country_of_residence = db.Column(db.String(500))

    # "date_of_birth": { nullable
    #     "day": "integer",
    #     "month": "integer",
    #     "year": "integer"
    # },

    dob_day = db.Column(db.Integer)
    dob_month = db.Column(db.Integer)
    dob_year = db.Column(db.Integer)

    # "etag": "string",

    etag = db.Column(db.String(500))

    # "identification": { nullable
    #     "country_registered": "string", nullable
    #     "legal_authority": "string",
    #     "legal_form": "string",
    #     "place_registered": "string", nullable
    #     "registration_number": "string" nullable
    # },

    id_country_registered = db.Column(db.String(500))
    id_legal_authority = db.Column(db.String(500))
    id_legal_form = db.Column(db.String(500))
    id_place_registered = db.Column(db.String(500))
    id_registration_number = db.Column(db.String(500))

    # "kind": "string",

    kind = db.Column(db.String(500))

    # "links": {
    #     "self": "string",
    #     "statement": "string"
    # },

    link_self = db.Column(db.String(500))
    link_statement = db.Column(db.String(500))

    # "name": "string",

    name = db.Column(db.String(500))

    # "name_elements": { nullable
    #     "forename": "string",
    #     "other_forenames": "string",
    #     "surname": "string",
    #     "title": "string"
    # },

    forename = db.Column(db.String(500))
    other_forenames = db.Column(db.String(500))
    surname = db.Column(db.String(500))
    title = db.Column(db.String(500))

    # "nationality": "string", nullable

    nationality = db.Column(db.String(500))

    # "natures_of_control": [
    #     "string"
    # ],

    # "notified_on": "date"

    notified_on = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)


def __repr__(self):
    return '<Person %r>' % self.name
