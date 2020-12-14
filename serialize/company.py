from flask_restx import Model, fields


company = Model('Company', {
    'companyName': fields.String(required=True, attribute='company_name'),
    'companyNumber': fields.String(attribute='company_number'),
    'addressLine1': fields.String(attribute='reg_address_address_line1'),
    'addressLine2': fields.String(attribute='reg_address_address_line2'),
    'addressPostTown': fields.String(attribute='reg_address_post_town'),
    'addressCounty': fields.String(attribute='reg_address_county'),
    'addressCountry': fields.String(attribute='reg_address_country'),
    'addressPostCode': fields.String(attribute='reg_address_post_code'),
    'companyCategory': fields.String(attribute='company_category'),
    'companyStatus': fields.String(attribute='company_status'),
    'countryOfOrigin': fields.String(attribute='country_of_origin'),
    'incorporationDate': fields.String(attribute='incorporation_date'),
    'sicCode': fields.String(attribute='sic_code_sic_text_1'),
    'uri': fields.String()
})
