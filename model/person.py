from .orm import db
from .nature_of_control import NatureOfControl


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    company_number = db.Column(db.String(8), db.ForeignKey(
        'company.company_number'), nullable=False)

    address_line_1 = db.Column(db.String(50))
    address_line_2 = db.Column(db.String(50))
    address_care_of = db.Column(db.String(60))
    address_country = db.Column(db.String(50))
    address_locality = db.Column(db.String(50))
    address_po_box = db.Column(db.String(12))
    address_postal_code = db.Column(db.String(15))
    address_premises = db.Column(db.String(50))
    address_region = db.Column(db.String(50))

    ceased_on = db.Column(db.DateTime)
    country_of_residence = db.Column(db.String(50))

    dob_day = db.Column(db.Integer)
    dob_month = db.Column(db.Integer)
    dob_year = db.Column(db.Integer)

    etag = db.Column(db.String(50))

    id_country_registered = db.Column(db.String(50))
    id_legal_authority = db.Column(db.String(50))
    id_legal_form = db.Column(db.String(50))
    id_place_registered = db.Column(db.String(50))
    id_registration_number = db.Column(db.String(50))

    kind = db.Column(db.String(50))

    link_self = db.Column(db.String(100))
    link_statement = db.Column(db.String(100))

    name = db.Column(db.String(100))

    forename = db.Column(db.String(50))
    other_forenames = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    title = db.Column(db.String(50))

    nationality = db.Column(db.String(50))

    natures_of_control = db.relationship(
        'NatureOfControl', backref=db.backref('person', lazy=True), lazy=True, cascade="all,delete")

    notified_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Person %r>' % self.name
