# -*- coding: utf-8 -*-
import codecs
import pymongo

connection = pymongo.MongoClient('localhost')

db = connection.candidatos2014

collection = db.clean_bienes

cursor = collection.find()

of = codecs.open('output/bienes.csv', 'w', 'utf-8')
index = 0
for candidato in cursor:
    obj = dict()
    obj['candidato_id'] = str(candidato['candidato_id'])
    obj['num_bienes_inmueble'] = str(candidato['num_bienes_inmueble'])
    obj['valor_bienes_inmueble'] = str(candidato['valor_bienes_inmueble'])
    obj['num_bienes_mueble'] = str(candidato['num_bienes_mueble'])
    obj['valor_bienes_mueble'] = str(candidato['valor_bienes_mueble'])

    if index == 0:
        s = ','.join('\"'+x+'\"' for x in obj.keys())
        of.write(s)
        of.write('\n')

    s = ','.join('\"'+unicode(x)+'\"' for x in obj.values())
    of.write(s)
    of.write('\n')
    
    index = index + 1
of.close()

