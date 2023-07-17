import psycopg2 as db
import pandas as pd

conn = db.connect(dbname='sige', user='marcos.albano', password='Albano@1971', port='5432', host='172.28.1.160')
cursor = conn.cursor()

cursor.execute('SELECT * FROM sige.lotes WHERE municipio_id = 2300101 LIMIT 10')
resultado = cursor.fetchall()

df = pd.DataFrame.from_dict(resultado)

print(df)

cursor.close()

