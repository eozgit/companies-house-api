from box import Box
from model.company import Company
from model.person import Person
from model.nature_of_control import NatureOfControl
from model.orm import db
from house import app

psc_file = 'psc-snapshot-2020-12-12_10of18.txt'

# all = ['individual-person-with-significant-control',
#        'legal-person-person-with-significant-control',
#        'corporate-entity-person-with-significant-control',
#        'super-secure-person-with-significant-control',
#        'persons-with-significant-control-statement',
#        'exemptions',
#        'totals#persons-of-significant-control-snapshot']

kinds = ['individual-person-with-significant-control',
         'legal-person-person-with-significant-control',
         'corporate-entity-person-with-significant-control']


with app.app_context():
    with open('setup/' + psc_file) as lines:
        count = 0
        for line in lines:
            record = Box.from_json(line)
            if record.data.kind not in kinds:
                continue

            company = Company.query.get(record.company_number)
            if company is None:
                continue

            data = record.data
            person = Person()
            person.company = company

            address = data.address
            if 'address_line_1' in address:
                person.address_line_1 = address.address_line_1
            if 'address_line_2' in address:
                person.address_line_2 = address.address_line_2
            if 'care_of' in address:
                person.address_care_of = address.care_of
            if 'country' in address:
                person.address_country = address.country
            if 'locality' in address:
                person.address_locality = address.locality
            if 'po_box' in address:
                person.address_po_box = address.po_box
            if 'postal_code' in address:
                person.address_postal_code = address.postal_code
            if 'premises' in address:
                person.address_premises = address.premises
            if 'region' in address:
                person.address_region = address.region

            if 'ceased_on' in data:
                person.ceased_on = data.ceased_on

            if 'country_of_residence' in data:
                person.country_of_residence = data.country_of_residence

            if 'date_of_birth' in data:
                date_of_birth = data.date_of_birth
                if 'day' in date_of_birth:
                    person.dob_day = date_of_birth.day
                if 'month' in date_of_birth:
                    person.dob_month = date_of_birth.month
                if 'year' in date_of_birth:
                    person.dob_year = date_of_birth.year

            person.etag = data.etag

            if 'id' in data:
                identification = data.id
                if 'country_registered' in identification:
                    person.id_country_registered = identification.country_registered
                if 'legal_authority' in identification:
                    person.id_legal_authority = identification.legal_authority
                if 'legal_form' in identification:
                    person.id_legal_form = identification.legal_form
                if 'place_registered' in identification:
                    person.id_place_registered = identification.place_registered
                if 'registration_number' in identification:
                    person.id_registration_number = identification.registration_number

            person.kind = data.kind

            links = data.links
            if 'self' in links:
                person.link_self = links.self
            if 'statement' in links:
                person.link_statement = links.statement

            person.name = data.name

            if 'name_elements' in data:
                name_elements = data.name_elements
                if 'forename' in name_elements:
                    person.forename = name_elements.forename
                if 'other_forenames' in name_elements:
                    person.other_forenames = name_elements.other_forenames
                if 'surname' in name_elements:
                    person.surname = name_elements.surname
                if 'title' in name_elements:
                    person.title = name_elements.title

            if 'nationality' in data:
                person.nationality = data.nationality

            person.notified_on = data.notified_on

            if 'natures_of_control' in data:
                for nature in data.natures_of_control:
                    NatureOfControl(nature_of_control=nature, person=person)

            count += 1
            if count > 1000:
                db.session.commit()
                break
