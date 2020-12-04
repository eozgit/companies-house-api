import psycopg2

path = './setup/BasicCompanyDataAsOneFile-2020-12-01.csv'

conn = psycopg2.connect('postgresql://postgres:postgres@localhost/postgres')
cur = conn.cursor()
copy_sql = """
           COPY Basic FROM stdin WITH CSV HEADER
           DELIMITER as ','
           """
with open(path, 'r') as f:
    cur.copy_expert(sql=copy_sql, file=f)
    conn.commit()
    cur.close()
