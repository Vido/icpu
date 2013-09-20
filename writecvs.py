# -*- coding: utf-8 -*- 

import csv
import sqlite3

conn = sqlite3.connect('db')
c = conn.cursor()

query = "select * from t_resumo;"
qs = c.execute(query)

with open('resumo.csv', 'w') as fp:
    fwriter = csv.writer(fp, delimiter=';', quotechar='"')
    for q in qs:
        try:
            fwriter.writerow(q)
        except:
            pass
   
