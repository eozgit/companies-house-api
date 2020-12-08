from flask_sqlalchemy import SQLAlchemy
from .orm import db


class NatureOfControl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey(
        'person.id'), nullable=False)
    person = db.relationship('Person', backref=db.backref(
        'natures_of_control', lazy=True))
    nature_of_control = db.Column(db.String(500))


def __repr__(self):
    return '<NatureOfControl %r %r>' % self.id % self.nature
