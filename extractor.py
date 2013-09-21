import csv
import sqlite3


def format_query(table, rows, reals_indexes):
    q ="INSERT INTO %s VALUES (" % table
    for row, i in zip(rows, range(len(rows))):
        if i == len(rows)-1:
            break
      
        try: 
            c_row = row.replace(',', '.') if ',' in row else row
            c_row = c_row.replace('\n', ' ') if '\n' in c_row else c_row
        except TypeError as e:
            c_row = row   
    

        if i not in reals_indexes:
            value = "'"+ c_row + "'"
        else:
            value = float(c_row)
             
        q += str(value) + ","

    query = q[:-1] + ");"
    return query


if __name__ == '__main__':

    conn = sqlite3.connect('db')
    c = conn.cursor()

    print 'data/SEGMENTOS_BRASILIA_T_DEFEITO.csv ...'

    with open('data/SEGMENTOS_BRASILIA_T_DEFEITO.csv', 'rb') as fp:
        csvfp = csv.reader(fp, 'excel', delimiter = ';')
        csvfp.next()

        for line in csvfp:
            try:
                query = format_query("T_DEFEITOS", line, [3])
                c.execute(query)
            except Exception as e:
                #print line
                print query
                print repr(e)

        conn.commit()

    print 'data/SEGMENTOS_BRASILIA_T_AVALIACAO.csv ...'

    with open('data/SEGMENTOS_BRASILIA_T_AVALIACAO.csv', 'r') as fp:
        csvfp = csv.reader(fp, 'excel', delimiter = ';')
        csvfp.next()

        for line in csvfp:
            try:
                query = format_query("T_AVALIACAO", line, [6])
                c.execute(query)
            except Exception as e:
                #print line
                print query
                print repr(e)

        conn.commit()


    print 'data/SEGMENTOS_BRASILIA_T_INVENTARIO.csv ...'

    with open('data/SEGMENTOS_BRASILIA_T_INVENTARIO.csv', 'r') as fp:
        csvfp = csv.reader(fp, 'excel', delimiter = ';')
        csvfp.next()

        for line in csvfp:
            try:
                query = format_query("T_INVENTARIO", line, [])
                c.execute(query)
            except Exception as e:
                #print line
                print query
                print repr(e)

        conn.commit()

    print 'data/SEGMENTOS_BRASILIA_T_SEGPISTA.csv ...'
    
    with open('data/SEGMENTOS_BRASILIA_T_SEGPISTA.csv', 'r') as fp:
        csvfp = csv.reader(fp, 'excel', delimiter = ';')
        csvfp.next()

        for line in csvfp:
            try:
                query = format_query("T_SEGPISTA", line, [])
                c.execute(query)
            except Exception as e:
                #print line
                print query
                print repr(e)

        conn.commit()

    conn.close()
