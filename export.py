# -*- coding: utf-8 -*-
import codecs
import pymongo
import json

connection = pymongo.MongoClient('localhost')

db = connection.candidatos2014

candidatos = db.candidatos

cursor = candidatos.find()
#cursor = candidatos.find().limit(10000)

of = codecs.open('output/candidatos.csv', 'w', 'utf-8')
index = 0
for candidato in cursor:
    obj = dict()
    obj['candidato_id'] = str(candidato['candidato_id'])
    obj['org_pol'] = json.dumps(candidato['d']['strRegistro_Org_Pol'])
    obj['cargo_autoridad'] = json.dumps(candidato['d']['objCargoAutoridadBE']['strCargoAutoridad'])
    obj['postula_ubigeo'] = json.dumps(candidato['d']['objUbigeoPostulaBE']['strUbigeo'])
    obj['postula_ubigeo_dep'] = json.dumps(candidato['d']['objUbigeoPostulaBE']['strDepartamento'])
    obj['postula_ubigeo_pro'] = json.dumps(candidato['d']['objUbigeoPostulaBE']['strProvincia'])
    obj['postula_ubigeo_dis'] = json.dumps(candidato['d']['objUbigeoPostulaBE']['strDistrito'])
    obj['forma_designacion'] = json.dumps(candidato['d']['strFormaDesignacion'])
    obj['dni'] = json.dumps(candidato['d']['strDNI'])
    obj['appaterno'] = json.dumps(candidato['d']['strAPaterno'])
    obj['apmaterno'] = json.dumps(candidato['d']['strAMaterno'])
    obj['nombres'] = json.dumps(candidato['d']['strNombres'])
    obj['fdn'] = json.dumps(candidato['d']['strFecha_Nac'])
    obj['sexo'] = str(candidato['d']['intId_Sexo'])
    obj['email'] = json.dumps(candidato['d']['strCorreo'])
    #nacimiento
    obj['nac_pais'] = json.dumps(candidato['d']['strPais'])
    obj['nac_ubigeo'] = json.dumps(candidato['d']['objUbigeoNacimientoBE']['strUbigeo'])
    obj['nac_ubigeo_dep'] = json.dumps(candidato['d']['objUbigeoNacimientoBE']['strDepartamento'])
    obj['nac_ubigeo_pro'] = json.dumps(candidato['d']['objUbigeoNacimientoBE']['strProvincia'])
    obj['nac_ubigeo_dis'] = json.dumps(candidato['d']['objUbigeoNacimientoBE']['strDistrito'])
    #residencia
    obj['residencia'] = json.dumps(candidato['d']['strResidencia'])
    obj['residencia_ubigeo'] = json.dumps(candidato['d']['objUbigeoResidenciaBE']['strUbigeo'])
    obj['residencia_ubigeo_dep'] = json.dumps(candidato['d']['objUbigeoResidenciaBE']['strDepartamento'])
    obj['residencia_ubigeo_pro'] = json.dumps(candidato['d']['objUbigeoResidenciaBE']['strProvincia'])
    obj['residencia_ubigeo_dis'] = json.dumps(candidato['d']['objUbigeoResidenciaBE']['strDistrito'])
    obj['residencia_tiempo'] = json.dumps(candidato['d']['strTiempo_Residencia'])
    #obj[] = candidato['d']['']
    #obj[] = candidato['d']['']


    if index == 0:
        s = ','.join('\"'+x+'\"' for x in obj.keys())
        of.write(s)
        of.write('\n')

    #s = ','.join('\"'+unicode(x)+'\"' for x in obj.values())
    s = ','.join(obj.values())
    of.write(s)
    of.write('\n')
    
    index = index + 1
of.close()

