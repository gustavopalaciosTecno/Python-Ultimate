from io import open

# escritura
# texto = "Hola Mundo"

# archivo = open("archivos/archivo-prueba.txt", "w")
# archivo.write(texto)
# archivo.close()

#lectura
# archivo = open("archivos/archivo-prueba.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

#lectura como lista
# archivo = open("archivos/archivo-prueba.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

#  aplicar método mágico
# with open("archivos/archivo-prueba.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0) # se usa para mover el puntero al comienzo
#     for linea in archivo:
#         print(linea)
 
#agregar texto   
# archivo = open("archivos/archivo-prueba.txt", "a+")
# texto = archivo.write("\nBye bye world")
# archivo.close()


# lectura y escritura del archivo
with open("archivos/archivo-prueba.txt", "r+") as archivo:
    texto = archivo.readlines()
    # archivo.seek(0)
    # texto[0] = "hola comadreja feliz :)"
    texto[0] = "\nhello world"
    print(texto)
    archivo.writelines(texto)
