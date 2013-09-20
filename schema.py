import sqlite3

conn = sqlite3.connect('db')
c = conn.cursor()

# T_DEFEITOS
c.execute('''
    CREATE TABLE T_DEFEITOS(
        RA30 text,
        CODIGO_DEFEITO text,
        FAIXA_ANALISADA text,
        EXTENSAO real,
        VERIFICAR text,
        CODIGO_SEVERIDADE text,
        CODIGO_TIPO_DEFEITO text,
        PD_AVALIADOR text,
        PD_PONDERADOS text,
        CODIGO_AVALIACAO text,
        FATOR_UTILIZADO text,
        CODIGO_SEGMENTO_PISTA text
    )'''
)

# T_AVALIACAO 
c.execute('''
    CREATE TABLE T_AVALIACAO(
        A30 text,
        CODIGO_AVALIACAO text,
        CODIGO_SEGMENTO_PISTA text,
        ICP_PD text,
        ACEITABILIDADE text,
        OBSERVACAO text,
        ICP_AV real,
        MES text,
        ANO text,
        AVALIACAO_COMPLEMENTAR text,
        DATA_AVALIACAO text,
        TOTAL_PD_AV text,
        CODIGO_ICP_CT text,
        CODIGO_MR_PREVISTA text,
        CODIGO_FUNCIONARIO_DIGITADOR text,
        CODIGO_FUNCIONARIO_AVALIADOR text,
        QTDE_DEF text,
        DATA_DIG text,
        ID_DIGITADOR text,
        OBS1 text,
        ICP_SE text,
        TOTAL_SE text,
        PONTOS_SE text,
        CODIGO_PARAM_CHECAGEM text,
        CODIGO_TP_AVALIACAO text,
        TOTAL_PD text
    )'''
)

# T_INVENTARIO
c.execute('''
    CREATE TABLE t_inventario(
        RA30 text,
        CODIGO_INVENTARIO text,
        CODIGO_SEGMENTO_PISTA text,
        CODIGO_PAVIMENTO text,
        CODIGO_VOLUME text,
        CODIGO_ROTA text,
        DATA_ANALISE text,
        NOME_RUA text,
        COMPRIMENTO text,
        LARGURA_PISTA text,
        IDADE text,
        ANO_ULTIMA_MR text,
        CODIGO_MR text,
        CODIGO_POCOVISITA text,
        CODIGO_INTERFERENCIA text,
        CODIGO_CALCADA text,
        CODIGO_DRENAGEM text,
        CODIGO_SUBLEITO text,
        CODIGO_ESTRUTURA text,
        CODIGO_SENTIDO text,
        CODIGO_GRID text,
        DA_RUA text,
        ATE_RUA text,
        NUMERO_FAIXAS text,
        RAIZ text,
        BOCA_LOBO text,
        CODIGO_CONDICAO_DRENAGEM text,
        CODIGO_ESTACIONAMENTO text,
        CODIGO_MEIOFIO text,
        CODIGO_CONDICAO_MEIOFIO text,
        CODIGO_CONDICAO_CALCADA text,
        CODIGO_HIERARQUIA text,
        VELOCIDADE_VIA text,
        VEICULOS_PESADOS text
    )'''
)

# T_SEGPISTA
c.execute('''
    CREATE TABLE t_segpista(
        OBJECTID text,
        SHAPE text,
        CODIGO_SEGMENTO_PISTA text,
        CodLog text,NomeLog text,
        NomeSegPista text,
        Principal text,
        Complemento text,
        CD_REG_ADM text,
        TipoPavimento text,
        TipoHierarquia text,
        TipoVia text,
        Status text,
        Fonte text,
        Dominio text,
        SHAPE_Length text,
        Enabled text,
        Grid text,
        Setor text,
        ClasseFuncional text,
        Ano_Construido text
    )'''
)

conn.close()
