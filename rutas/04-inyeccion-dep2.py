from pathlib import Path


path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

def load(p):
   
    paquete = __import__(str(p).replace("/", "."))
    paquete.init()

list(map(load, paths))