from model.orm import db
from model.company import Company
from model.person import Person
from model.nature_of_control import NatureOfControl
from house import app

with app.app_context():
    db.drop_all()
    db.create_all()
