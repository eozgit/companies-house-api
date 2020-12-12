import psycopg2

path = './setup/BasicCompanyData-2020-12-01-part4_6.csv'

conn = psycopg2.connect('postgresql://postgres:postgres@localhost/postgres')
cur = conn.cursor()
copy_sql = """
           COPY company FROM stdin WITH CSV HEADER
           DELIMITER as ','
           """
with open(path, 'r') as f:
    cur.copy_expert(sql=copy_sql, file=f)
    conn.commit()
    cur.close()
