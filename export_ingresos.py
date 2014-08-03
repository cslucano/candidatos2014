# -*- coding: utf-8 -*-
import codecs
import pymongo

connection = pymongo.MongoClient('localhost')

db = connection.candidatos2014

collection = db.clean_ingresos

cursor = collection.find()

of = codecs.open('output/ingresos.csv', 'w', 'utf-8')
index = 0
for candidato in cursor:
    obj = dict()
    obj['candidato_id'] = str(candidato['candidato_id'])
    obj['remuneracionPublico'] = str(candidato['remuneracionPublico'])
    obj['remuneracionPrivado'] = str(candidato['remuneracionPrivado'])
    obj['rentaPublico'] = str(candidato['rentaPublico'])
    obj['rentaPrivado'] = str(candidato['rentaPrivado'])
    obj['otrosPublico'] = str(candidato['otrosPublico'])
    obj['otrosPrivado'] = str(candidato['otrosPrivado'])

    if index == 0:
        s = ','.join('\"'+x+'\"' for x in obj.keys())
        of.write(s)
        of.write('\n')

    s = ','.join('\"'+unicode(x)+'\"' for x in obj.values())
    of.write(s)
    of.write('\n')
    
    index = index + 1
of.close()

