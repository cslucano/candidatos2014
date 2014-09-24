import sys
import json
import urllib2
import urllib
import pymongo

connection = pymongo.MongoClient('localhost')
db = connection.candidatos2014
collection = db.foto

dataDict = json.loads('{"objCandidatoBE": {"objProcesoElectoralBE": {"intIdProceso": "72"}, "objOpInscritasBE": { "intCod_OP": "140"}, "objAmbitoBE": {}, "objCargoAutoridadBE": {}, "objUbigeoPostulaBE": {}, "objUbigeoNacimientoBE": {}, "objUbigeoResidenciaBE": {}, "objUsuarioBE": {}, "intId_Candidato": "104272" }}')

url_be_candidato = 'http://200.48.102.67/pecaoe/servicios/declaracion.asmx/CandidatoListarPorID'
url_be_foto = 'http://200.48.102.67/pecaoe/servicios/declaracion.asmx/CandidatoFotoListarPorID'
url_reniec = 'http://200.48.102.67/pecaoe/servicios/declaracion.asmx/ObtenerRutaFotoDNI'
url_foto = 'http://200.48.102.67/pecaoe/06FOTOS/2014/'

headers = {'Content-Type': 'application/json'}
#for i in range(1, 116827):
#for i in range(1, 10000):
#for i in range(10000, 30000):
#for i in range(30000, 80000):
for i in range(80605, 116827):
    try:
        dataDict['objCandidatoBE']['intId_Candidato'] = str(i)
        data = json.dumps(dataDict)

        req = urllib2.Request(url_be_foto, data, headers)
        response = urllib2.urlopen(req).read()

        collectionJson = json.loads(response)
        collectionJson['candidato_id'] = i

        collection.insert(collectionJson)
        f_name = collectionJson['d']['strArchivo']
        url_f = url_foto + f_name

        if '0' == collectionJson['d']['strFotoPadron']:
            ##print url_f
            urllib.urlretrieve(url_f, 'fotos/' + str(i) + '_' + f_name)
        else:
            req = urllib2.Request(url_be_candidato, data, headers)
            response = urllib2.urlopen(req).read()
            candidatoJson = json.loads(response)

            fotoDict = json.loads('{"objCandidatoBE": {"strDNI": ""}}')
            fotoDict['objCandidatoBE']['strDNI'] = candidatoJson['d']['strDNI']
            dni_load = json.dumps(fotoDict)

            req = urllib2.Request(url_reniec, dni_load, headers)
            response = urllib2.urlopen(req).read()

            fotoJson = json.loads(response)
            url_f = fotoJson['d'][0]
            urllib.urlretrieve(url_f, 'fotos/' + str(i) + '_' + f_name)

    except:
        print i
        print "Error: ", sys.exc_info()[0]
