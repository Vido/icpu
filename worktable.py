import sqlite3
from extractor import format_query

conn = sqlite3.connect('db')
c = conn.cursor()

try:
    query = '''
        CREATE TABLE T_RESUMO(
            CODIGO_SEGMENTO_PISTA text,
            TIPO_DEFEITO text,
            PESO_DEFEITO real,
            CODIGO_SEVERIDADE text,
            FATOR_SEVERIDADE real,
            SHAPE_LENGTH real,
            LARGURA_PISTA real,
            AREA_SEGMENTO real,
            AREA_DEFEITO real,
            PORCENTAGEM_DEFEITO real,
            CODIGO_EXTENSAO text,
            ICP_AV real
        )
    '''

    # AREA_SEGMENTO = SHAPE * LARGURA
    # PORCENTAGEM_DEFEITO = AREA_DEFEITO / AREA_SEGMENTO
    # NIVEL_EXTENSAO = (1, 2, 3)

    # if TIPO_DEFEITO in (4, 14):
    #     AREA_DEFEITO = AREA_DEFEITO * 0.5

    qs = c.execute(query)

except sqlite3.OperationalError as e:
    print repr(e)
    pass


query = '''
    select 
        d.CODIGO_SEGMENTO_PISTA,
        d.CODIGO_TIPO_DEFEITO,
        d.CODIGO_SEVERIDADE,
        s.SHAPE_LENGTH,
        i.LARGURA_PISTA,
        d.EXTENSAO,
        a.ICP_AV
    from
        t_defeitos as d,
        t_avaliacao as a,
        t_inventario as i,
        t_segpista as s
    where 
        d.CODIGO_SEGMENTO_PISTA=a.CODIGO_SEGMENTO_PISTA
        and
        d.CODIGO_SEGMENTO_PISTA=i.CODIGO_SEGMENTO_PISTA
        and
        d.CODIGO_SEGMENTO_PISTA=s.CODIGO_SEGMENTO_PISTA
        and
        i.CODIGO_PAVIMENTO="1"
         ;
'''

qs = c.execute(query).fetchall()

MODELO_PESOS = [
    {'':''},
    {'PESO': 11, 1: 0.53, 2: 0.76, 3: 1.0}, # Trincas por Fadiga
    {'PESO':  6, 1: 0.29, 2: 0.55, 3: 1.0}, # Trincas em Bloco
    {'PESO':  5, 1: 0.26, 2: 0.61, 3: 1.0}, # Defeitos nos Bordos
    {'PESO':  5, 1: 0.23, 2: 0.49, 3: 1.0}, # Trincas Longitudinais
    {'PESO':  7, 1: 0.21, 2: 0.52, 3: 1.0}, # Trincas por Reflexao
    {'PESO':  5, 1: 0.23, 2: 0.49, 3: 1.0}, # Trincas Transversais
    {'PESO':  8, 1: 0.27, 2: 0.60, 3: 1.0}, # Remendos
    {'PESO': 12, 1: 0.58, 2: 0.81, 3: 1.0}, # Panelas
    {'PESO': 12, 1: 0.44, 2: 0.72, 3: 1.0}, # Deformacao Permanente
    {'PESO':  7, 1: 0.23, 2: 0.62, 3: 1.0}, # Corrugacao
    {'PESO':  4, 1: 0.19, 2: 0.53, 3: 1.0}, # Exudacao
    {'PESO':  4, 1: 0.20, 2: 0.57, 3: 1.0}, # Agregados Polidos
    {'PESO':  5, 1: 0.14, 2: 0.49, 3: 1.0}, # Desgaste
    {'PESO':  4, 1: 0.35, 2: 0.49, 3: 1.0}, # Desnivel
    {'PESO':  5, 1: 1.00, 2: 1.00, 3: 1.0}, # Bombeamento
]

resumo = []

for q in qs:
    codigo = q[0]
    tipo = q[1]
    peso = str(MODELO_PESOS[int(q[1])]['PESO'])
    codigo_sev = q[2]
    fator_sev = float(MODELO_PESOS[int(q[1])][int(q[2])])
    print fator_sev
    shape_l = q[3]
    largura = q[4]

    area_seg = float(shape_l) * float(largura)
    area_defeito = float(q[5]) * 0.5 if tipo in ['4', '14'] else float(q[5])
    proc_defeito = (area_defeito * 100) / area_seg

    nivel = "1"
    if proc_defeito > 10: 
        nivel = "2"
    if proc_defeito > 50: 
        nivel = "3"

    icpav = str(q[6])

    l = [
        codigo,
        tipo,
        peso,
        codigo_sev,
        fator_sev,
        shape_l,
        largura,
        area_seg,
        area_defeito,
        proc_defeito,
        nivel,
        icpav,
        "\n"
    ]
    #print l
    resumo.append(l)
    

for row in resumo:
    query = format_query("T_RESUMO", row, [2, 4, 5, 6, 7, 8, 9, 11])
    print query
    c.execute(query)

conn.commit()

print "Total de registros: ",
print c.execute("select count(*) from T_RESUMO;").fetchall()
print "Amostra: ",
print c.execute("select * from T_RESUMO LIMIT 4").fetchall()

