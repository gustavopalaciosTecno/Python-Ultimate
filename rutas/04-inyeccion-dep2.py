from pathlib import Path
from rutas.uno import graphql
from rutas.dos import db, api
# import db
# import api
# import graphql

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db":db,
    "api":api,
    "graphql":graphql
}

def load(p):
   
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("el paquete no tiene función init")        

list(map(load, paths))