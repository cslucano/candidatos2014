# -*- coding: utf-8 -*-
import codecs
import pymongo
import psycopg2
import re

def replace_tab(string):
  return re.sub(r'\t', ' ', string)

pgconn = psycopg2.connect(host='localhost', dbname='e2014', user='e2014', password='e2014')
pgcur = pgconn.cursor()

mgconn = pymongo.MongoClient('localhost')
db = mgconn.candidatos2014
collection = db.bienes
cursor = collection.find()

for candidato in cursor:
    if not (len(candidato['d']) > 0): 
        continue

        pgcur.execute(
            "INSERT INTO bien_stage(candidatojneid, idbien, nombre, descripcion, caracteristicas, valor) values (%s, %s, %s, %s, %s, %s)", (
              candidato['candidato_id'],
              item['intId_Bien'],
              item['strNombre_Bien'],
              item['strDescripcion_Bien'],
              item['strCaracteristicas_Bien'],
              item['floValor_Bien'], 
            )
        )

        pgconn.commit()

pgconn.close()
mgconn.close()
