from pprint import pprint
"""
1. Eliminar los espacios en blanco de un string y devolver una lista con los caracteres correspondiente
2. Contar con un diccionario cuanto se repiten los caracteres de un string
3. Ordenar las llaves de un diccionario por el valor que tienen y dveolver una lista
que contiene tuplas [("a", 3), ("b", 2), ("c", 4), ("d",4)]
4. de un listado de tuplas, devolver las tuplas que contengan el mayor valor 
[("a", 3), ("b", 2), ("c", 4), ("d",4)]-> [("c",4)]
5. Crear un mensaje que diga:
los caracteres que mas se repiten con 4 repeticiones son:
- C
- D
"""

#1. Eliminar los espacios en blanco de un string y devolver una lista con los caracteres correspondiente
string = "hola mundo este es mi string"

def quita_espacios(texto):
   return [char for char in texto if char != " "]

sin_espacios = quita_espacios(string)
print(sin_espacios)

# 2. Contar con un diccionario cuanto se repiten los caracteres de un string
def cuenta_caracteres(lista):
   chars_dict = {}
   for char in lista:
      if char in chars_dict:
         chars_dict[char]+=1
      else:
         chars_dict[char] = 1   
   return chars_dict
# 3. Ordenar las llaves de un diccionario por el valor que tienen y dveolver una lista
# que contiene tuplas [("a", 3), ("b", 2), ("c", 4), ("d",4)]

def ordena(dict):
       return sorted(
      dict.items(),
      key=lambda key:key[1],
      reverse=True
   )

# 4. de un listado de tuplas, devolver las tuplas que contengan el mayor valor 
# [("a", 3), ("b", 2), ("c", 4), ("d",4)]-> [("c",4)]

def mayores_tuplas(lista):
       maximo = lista[0][1]
       respuesta = {}
       for orden in lista:
              if maximo > orden[1]:
                     break
              respuesta[orden[0]] = orden[1]
       return respuesta              
         
# 5. Crear un mensaje que diga:
# los caracteres que mas se repiten con 4 repeticiones son:
# - C
# - D                                 

def crea_mensaje(diccionario):
       mensaje = "los que mas se repiten son: \n"
       for key, valor in diccionario.items():
              mensaje+= f"- {key} con {valor} repeticiones \n"
       return mensaje
                  
                 
sin_espacios = quita_espacios(string)
contados = cuenta_caracteres(sin_espacios)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
print(mensaje)



