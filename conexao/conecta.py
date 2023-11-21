import psycopg2 as db
import pandas as pd

conn = db.connect(dbname='sige', user='postgres', password='Axp@01fal12', port='5432', host='localhost')
cursor = conn.cursor()

cursor.execute(
    """SELECT DISTINCT ON (l.id) l.id AS lote_id, m.nome AS nome_municipio, terr.nom_territorio 
        FROM sige.titulos t JOIN sige.lotes l ON l.id = t.lote_id 
        JOIN ibge.municipios m ON m.id = l.municipio_id 
        JOIN nom.territorio_mun tm ON tm.cod_mun = m.id 
        JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio 
        JOIN sige.situacoes_juridicas sj ON sj.id = l.situacao_juridica_id 
        WHERE l.projeto_especial = false AND t.flag_cancelamento <> 'S' AND m.uf = 'CE'
    """
)

resultado = cursor.fetchall()

df_sige = pd.DataFrame.from_dict(resultado)

# print(df)

cursor.close()

