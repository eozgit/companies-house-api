from flask_sqlalchemy import SQLAlchemy
from .orm import db


class NatureOfControl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)
    nature_of_control = db.Column(db.String(100))


def __repr__(self):
    return '<NatureOfControl %r %r>' % self.id % self.nature
