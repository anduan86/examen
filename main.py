import requests
from consulta import get_equipo
from mongo import MongoConnection

equipos = ["drtech", "medisono", "samsung", "ge", "canon", "philips"]
db_client = MongoConnection().client
db = db_client.get_database('examen')
col = db.get_collection('equipos')
for t in equipos:
    get_equipo(equipo=t, verbose=True)
    document = {
        "equipo": equipos
    }

    col.insert_one(document=document)


for t in equipos:
    get_equipo(equipo=t, verbose=True)
