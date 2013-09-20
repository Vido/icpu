import sys
import sqlite3
from extractor import format_query

conn = sqlite3.connect('db')
c = conn.cursor()

try:
    query = '''
        CREATE TABLE T_RESUMO(
            CODIGO_SEGMENTO_PISTA text,
            TIPO_DEFEITO text,
            PESO real,
            SEVERIDADE text,
            ICP_AV real
        )
    '''
    qs = c.execute(query)

except sqlite3.OperationalError as e:
    print repr(e)
    pass


query = '''
    select 
        d.CODIGO_SEGMENTO_PISTA,
        d.CODIGO_TIPO_DEFEITO,
        a.ICP_AV
    from
        t_defeitos as d,
        t_avaliacao as a,
        t_inventario as i
    where 
        d.CODIGO_SEGMENTO_PISTA=a.CODIGO_SEGMENTO_PISTA
        and
        d.CODIGO_SEGMENTO_PISTA=i.CODIGO_SEGMENTO_PISTA
         ;
'''

qs = c.execute(query).fetchall()

MODELO_PESOS = [
    {'':''},
    {'PESO': 11, 'BAIXA': 0.53, 'MEDIA': 0.76, 'ALTA': 1.0}, # Trincas por Fadiga
    {'PESO':  6, 'BAIXA': 0.29, 'MEDIA': 0.55, 'ALTA': 1.0}, # Trincas em Bloco
    {'PESO':  5, 'BAIXA': 0.26, 'MEDIA': 0.61, 'ALTA': 1.0}, # Defeitos nos Bordos
    {'PESO':  5, 'BAIXA': 0.23, 'MEDIA': 0.49, 'ALTA': 1.0}, # Trincas Longitudinais
    {'PESO':  7, 'BAIXA': 0.21, 'MEDIA': 0.52, 'ALTA': 1.0}, # Trincas por Reflexao
    {'PESO':  5, 'BAIXA': 0.23, 'MEDIA': 0.49, 'ALTA': 1.0}, # Trincas Transversais
    {'PESO':  8, 'BAIXA': 0.27, 'MEDIA': 0.60, 'ALTA': 1.0}, # Remendos
    {'PESO': 12, 'BAIXA': 0.58, 'MEDIA': 0.81, 'ALTA': 1.0}, # Panelas
    {'PESO': 12, 'BAIXA': 0.44, 'MEDIA': 0.72, 'ALTA': 1.0}, # Deformacao Permanente
    {'PESO':  7, 'BAIXA': 0.23, 'MEDIA': 0.62, 'ALTA': 1.0}, # Corrugacao
    {'PESO':  4, 'BAIXA': 0.19, 'MEDIA': 0.53, 'ALTA': 1.0}, # Exudacao
    {'PESO':  4, 'BAIXA': 0.20, 'MEDIA': 0.57, 'ALTA': 1.0}, # Agregados Polidos
    {'PESO':  5, 'BAIXA': 0.14, 'MEDIA': 0.49, 'ALTA': 1.0}, # Desgaste
    {'PESO':  4, 'BAIXA': 0.35, 'MEDIA': 0.49, 'ALTA': 1.0}, # Desnivel
    {'PESO':  5, 'BAIXA': 1.00, 'MEDIA': 1.00, 'ALTA': 1.0}, # Bombeamento
]

resumo = []
for q in qs:
    codigo = q[0]
    tipo = q[1]
    #peso = MODELO_PESOS[]
    peso = str(MODELO_PESOS[int(q[1])]['PESO'])
    #severidade = MODELO_PESOS[int[1]]
    icpav = str(q[2])

    l = [codigo, tipo, peso, "SEVERIDADE", icpav, "\n"]
    resumo.append(l)
    

for row in resumo:
    query = format_query("T_RESUMO", row, [2, 4])
    c.execute(query)

conn.commit()

print "Total de registros: ",
print c.execute("select count(*) from T_RESUMO;").fetchall()
print "Amostra: ",
print c.execute("select * from T_RESUMO LIMIT 1;").fetchall()

