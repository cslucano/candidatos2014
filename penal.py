import sys
import json
import urllib2
import pymongo

connection = pymongo.MongoClient('localhost')
db = connection.candidatos2014
collection = db.penal
collection.drop()

dataDict = json.loads('{"objCandidatoBE": {"objProcesoElectoralBE": {"intIdProceso": "72"}, "objOpInscritasBE": { "intCod_OP": "140"}, "objAmbitoBE": {}, "objCargoAutoridadBE": {}, "objUbigeoPostulaBE": {}, "objUbigeoNacimientoBE": {}, "objUbigeoResidenciaBE": {}, "objUsuarioBE": {}, "intId_Candidato": "104272" }}')

url = 'http://200.48.102.67/pecaoe/servicios/declaracion.asmx/AmbitoPenalListarPorCandidato'
headers = {'Content-Type': 'application/json'}
#for i in range(1, 9):
for i in range(1, 116827):
    try:
        dataDict['objCandidatoBE']['intId_Candidato'] = str(i)
        data = json.dumps(dataDict)

        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req).read()

        collectionJson = json.loads(response)
        collectionJson['candidato_id'] = i

        collection.insert(collectionJson)
    except:
        print i
	print "Error: ", sys.exc_info()[0]
