from .orm import db
from .person import Person


class Company(db.Model):
    company_name = db.Column(db.String(160))
    company_number = db.Column(db.String(8), primary_key=True)
    reg_address_care_of = db.Column(db.String(82))
    reg_address_po_box = db.Column(db.String(10))
    reg_address_address_line1 = db.Column(db.String(101))
    reg_address_address_line2 = db.Column(db.String(70))
    reg_address_post_town = db.Column(db.String(50))
    reg_address_county = db.Column(db.String(50))
    reg_address_country = db.Column(db.String(37))
    reg_address_post_code = db.Column(db.String(15))
    company_category = db.Column(db.String(89))
    company_status = db.Column(db.String(48))
    country_of_origin = db.Column(db.String(24))
    dissolution_date = db.Column(db.String(10))  # DateTime
    incorporation_date = db.Column(db.String(10))  # DateTime
    accounts_account_ref_day = db.Column(db.String(2))  # Integer
    accounts_account_ref_month = db.Column(db.String(2))  # Integer
    accounts_next_due_date = db.Column(db.String(10))  # DateTime
    accounts_last_made_up_date = db.Column(db.String(10))  # DateTime
    accounts_account_category = db.Column(db.String(27))
    returns_next_due_date = db.Column(db.String(10))  # DateTime
    returns_last_made_up_date = db.Column(db.String(10))  # DateTime
    mortgages_num_mort_charges = db.Column(db.String(4))
    mortgages_num_mort_outstanding = db.Column(db.String(4))
    mortgages_num_mort_part_satisfied = db.Column(db.String(2))
    mortgages_num_mort_satisfied = db.Column(db.String(4))
    sic_code_sic_text_1 = db.Column(db.String(166))
    sic_code_sic_text_2 = db.Column(db.String(166))
    sic_code_sic_text_3 = db.Column(db.String(166))
    sic_code_sic_text_4 = db.Column(db.String(166))
    limited_partnerships_num_gen_partners = db.Column(db.String(3))
    limited_partnerships_num_lim_partners = db.Column(db.String(3))
    uri = db.Column(db.String(47))
    previous_name_1_condate = db.Column(db.String(10))  # DateTime
    previous_name_1_company_name = db.Column(db.String(160))
    previous_name_2_condate = db.Column(db.String(10))  # DateTime
    previous_name_2_company_name = db.Column(db.String(160))
    previous_name_3_condate = db.Column(db.String(10))  # DateTime
    previous_name_3_company_name = db.Column(db.String(102))
    previous_name_4_condate = db.Column(db.String(10))  # DateTime
    previous_name_4_company_name = db.Column(db.String(116))
    previous_name_5_condate = db.Column(db.String(10))  # DateTime
    previous_name_5_company_name = db.Column(db.String(107))
    previous_name_6_condate = db.Column(db.String(10))  # DateTime
    previous_name_6_company_name = db.Column(db.String(64))
    previous_name_7_condate = db.Column(db.String(10))  # DateTime
    previous_name_7_company_name = db.Column(db.String(64))
    previous_name_8_condate = db.Column(db.String(10))  # DateTime
    previous_name_8_company_name = db.Column(db.String(52))
    previous_name_9_condate = db.Column(db.String(10))  # DateTime
    previous_name_9_company_name = db.Column(db.String(52))
    previous_name_10_condate = db.Column(db.String(10))  # DateTime
    previous_name_10_company_name = db.Column(db.String(40))
    conf_stmt_next_due_date = db.Column(db.String(10))  # DateTime
    conf_stmt_last_made_up_date = db.Column(db.String(10))  # DateTime

    people = db.relationship("Person", backref=db.backref(
        "company", lazy=True), lazy=True, cascade="all,delete")

    def __repr__(self):
        return '<Company %r>' % self.company_name
