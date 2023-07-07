import csv

#escribir
# with open("archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["id_usuario", "name", "city"])
#     writer.writerow([100, "Gustavo", "Charata"])
#     writer.writerow([101, "María", "gral Pinedo"])
   
# leer
with open("archivos/archivo.csv") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for linea in reader:
        print(linea)    
    