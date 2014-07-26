import sys
import json
import urllib2
import pymongo

connection = pymongo.MongoClient('localhost')
db = connection.candidatos2014
ingresos = db.ingresos
ingresos.drop()

dataDict = json.loads('{"objCandidatoBE": {"objProcesoElectoralBE": {"intIdProceso": "72"}, "objOpInscritasBE": { "intCod_OP": "140"}, "objAmbitoBE": {}, "objCargoAutoridadBE": {}, "objUbigeoPostulaBE": {}, "objUbigeoNacimientoBE": {}, "objUbigeoResidenciaBE": {}, "objUsuarioBE": {}, "intId_Candidato": "104272" }}')

url = 'http://200.48.102.67/pecaoe/servicios/declaracion.asmx/IngresoListarPorCandidato'
headers = {'Content-Type': 'application/json'}
#for i in range(1, 9):
for i in range(1, 116827):
    try:
        dataDict['objCandidatoBE']['intId_Candidato'] = str(i)
        data = json.dumps(dataDict)

        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req).read()

        ingresosJson = json.loads(response)
        ingresosJson['candidato_id'] = i

        ingresos.insert(ingresosJson)
    except:
	print "Error: ", sys.exc_info()[0]
