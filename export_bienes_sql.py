# -*- coding: utf-8 -*-
import codecs
import pymongo
import re

def replace_tab(string):
  return re.sub(r'\t', ' ', string)

connection = pymongo.MongoClient('localhost')

db = connection.candidatos2014

collection = db.bienes

cursor = collection.find()

of = codecs.open('output/bienes.sql', 'w', 'utf-8')
index = 0
for candidato in cursor:
    if not (len(candidato['d']) > 0): 
        continue
    for item in candidato['d']:
        bien_line = ''
        bien_line = str(candidato['candidato_id'])
        bien_line += '\t' + str(item['intId_Bien'])
        bien_line += '\t' + replace_tab(item['strNombre_Bien'])
        bien_line += '\t' + replace_tab(item['strDescripcion_Bien'])
        bien_line += '\t' + replace_tab(item['strCaracteristicas_Bien'])
        bien_line += '\t' + str(item['floValor_Bien']) + '\n'

        index += 1
        print index

        of.write(bien_line)
of.close()

