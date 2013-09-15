import sqlite3
from extractor import format_query

conn = sqlite3.connect('db')
c = conn.cursor()

try:
    query = '''
        CREATE TABLE T_RESUMO(
            CODIGO_SEGMENTO_PISTA text,
            TIPO text,
            DEFEITO text,
            PESO text,
            SEVERIDADE text
        )
    '''
    qs = c.execute(query)

except sqlite3.OperationalError as e:
    pass


query = '''
    select 
        d.CODIGO_SEGMENTO_PISTA,
        d.CODIGO_TIPO_DEFEITO
    from t_defeitos as d, t_avaliacao as a 
    where d.CODIGO_SEGMENTO_PISTA=a.CODIGO_SEGMENTO_PISTA;
'''

qs = c.execute(query).fetchall()

resumo = []
for q in qs:
    lstq = list(q)
    lstq += ["DEFEITO", "PESO", "SEVERIDADE", "\n"]
    resumo.append(lstq)
    

for row in resumo:
    query = format_query("T_RESUMO", row, [])
    c.execute(query)

conn.commit()

print "Total de registros: ",
print c.execute("select count(*) from T_RESUMO;").fetchall()
