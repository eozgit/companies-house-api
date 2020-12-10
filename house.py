from flask import Flask
from flask_restx import Api, Resource, fields
from model.orm import db
from model.company_info import CompanyInfo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
api = Api(app)


company = api.model('Company', {
    'company_name': fields.String(required=True, description='Company name'),
    'company_number': fields.String(description='Company number'), 'reg_address_care_of': fields.String(),
    'reg_address_po_box': fields.String(),
    'reg_address_address_line1': fields.String(),
    'reg_address_address_line2': fields.String(),
    'reg_address_post_town': fields.String(),
    'reg_address_county': fields.String(),
    'reg_address_country': fields.String(),
    'reg_address_post_code': fields.String(),
    'company_category': fields.String(),
    'company_status': fields.String(),
    'country_of_origin': fields.String(),
    'dissolution_date': fields.String(),
    'incorporation_date': fields.String(),
    'accounts_account_ref_day': fields.String(),
    'accounts_account_ref_month': fields.String(),
    'accounts_next_due_date': fields.String(),
    'accounts_last_made_up_date': fields.String(),
    'accounts_account_category': fields.String(),
    'returns_next_due_date': fields.String(),
    'returns_last_made_up_date': fields.String(),
    'mortgages_num_mort_charges': fields.String(),
    'mortgages_num_mort_outstanding': fields.String(),
    'mortgages_num_mort_part_satisfied': fields.String(),
    'mortgages_num_mort_satisfied': fields.String(),
    'sic_code_sic_text_1': fields.String(),
    'sic_code_sic_text_2': fields.String(),
    'sic_code_sic_text_3': fields.String(),
    'sic_code_sic_text_4': fields.String(),
    'limited_partnerships_num_gen_partners': fields.String(),
    'limited_partnerships_num_lim_partners': fields.String(),
    'uri': fields.String(),
    'previous_name_1_condate': fields.String(),
    'previous_name_1_company_name': fields.String(),
    'previous_name_2_condate': fields.String(),
    'previous_name_2_company_name': fields.String(),
    'previous_name_3_condate': fields.String(),
    'previous_name_3_company_name': fields.String(),
    'previous_name_4_condate': fields.String(),
    'previous_name_4_company_name': fields.String(),
    'previous_name_5_condate': fields.String(),
    'previous_name_5_company_name': fields.String(),
    'previous_name_6_condate': fields.String(),
    'previous_name_6_company_name': fields.String(),
    'previous_name_7_condate': fields.String(),
    'previous_name_7_company_name': fields.String(),
    'previous_name_8_condate': fields.String(),
    'previous_name_8_company_name': fields.String(),
    'previous_name_9_condate': fields.String(),
    'previous_name_9_company_name': fields.String(),
    'previous_name_10_condate': fields.String(),
    'previous_name_10_company_name': fields.String(),
    'conf_stmt_next_due_date': fields.String(),
    'conf_stmt_last_made_up_date': fields.String()
})


@api.route('/house')
class House(Resource):
    def get(self):
        return {'house': 'companies'}


@api.route('/company/<string:id>')
class Company(Resource):
    @api.marshal_with(company)
    def get(self, id):
        return CompanyInfo.query.get_or_404(id)


if __name__ == '__main__':
    app.run(debug=True)
