# -*- coding: utf-8 -*-
import codecs
import pymongo

connection = pymongo.MongoClient('localhost')

db = connection.candidatos2014

candidatos = db.candidatos

#Todos los candidatos
#cursor = candidatos.find()

# Los que postulan en la provincia de LIMA
cursor = candidatos.find({'d.objUbigeoPostulaBE.strDepartamento': 'LIMA','d.objUbigeoPostulaBE.strProvincia': 'LIMA'})

# Los que postulan en el distrito de MAGDALENA DEL MAR - LIMA
#cursor = candidatos.find({'d.objUbigeoPostulaBE.strDepartamento': 'LIMA','d.objUbigeoPostulaBE.strProvincia': 'LIMA', 'd.objUbigeoPostulaBE.strDistrito': 'MAGDALENA DEL MAR'})

of = codecs.open('output/candidatos.csv', 'w', 'utf-8')
index = 0
for candidato in cursor:
    obj = dict()
    obj['candidato_id'] = str(candidato['candidato_id'])
    obj['org_pol'] = candidato['d']['strRegistro_Org_Pol']
    obj['cargo_autoridad'] = candidato['d']['objCargoAutoridadBE']['strCargoAutoridad']
    obj['ubigeo_postula_dep'] = candidato['d']['objUbigeoPostulaBE']['strDepartamento']
    obj['ubigeo_postula_pro'] = candidato['d']['objUbigeoPostulaBE']['strProvincia']
    obj['ubigeo_portula_dis'] = candidato['d']['objUbigeoPostulaBE']['strDistrito']
    obj['forma_designacio'] = candidato['d']['strFormaDesignacion']
    obj['dni'] = candidato['d']['strDNI']
    obj['appaterno'] = candidato['d']['strAPaterno']
    obj['apmaterno'] = candidato['d']['strAMaterno']
    obj['nombres'] = candidato['d']['strNombres']
    obj['fdn'] = candidato['d']['strFecha_Nac']
    obj['sexo'] = str(candidato['d']['intId_Sexo'])
    obj['email'] = candidato['d']['strCorreo']
    #nacimiento
    obj['nac_pais'] = candidato['d']['strPais']
    obj['nac_ubigeo_dep'] = candidato['d']['objUbigeoNacimientoBE']['strDepartamento']
    obj['nac_ubigeo_pro'] = candidato['d']['objUbigeoNacimientoBE']['strProvincia']
    obj['nac_ubigeo_dis'] = candidato['d']['objUbigeoNacimientoBE']['strDistrito']
    #residencia
    obj['residencia'] = candidato['d']['strResidencia']
    obj['residencia_ubigeo_dep'] = candidato['d']['objUbigeoResidenciaBE']['strDepartamento']
    obj['residencia_ubigeo_pro'] = candidato['d']['objUbigeoResidenciaBE']['strProvincia']
    obj['residencia_ubigoe_dis'] = candidato['d']['objUbigeoResidenciaBE']['strDistrito']
    obj['residencia_tiempo'] = candidato['d']['strTiempo_Residencia']
    #obj[] = candidato['d']['']
    #obj[] = candidato['d']['']


    if index == 0:
        s = ','.join('\"'+x+'\"' for x in obj.keys())
        of.write(s)
        of.write('\n')

    s = ','.join('\"'+unicode(x)+'\"' for x in obj.values())
    of.write(s)
    of.write('\n')
    
    index = index + 1
of.close()

