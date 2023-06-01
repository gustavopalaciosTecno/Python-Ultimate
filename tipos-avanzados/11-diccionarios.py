# en los diccionarios las llaves son string y los valores pueden ser cualquier dato
punto = {"x":25, "y":30}
print(punto)
print(punto["x"])

# crear una nueva llave
punto["z"] = 45
print(punto)

# usar una condicional para saber si el valor existe
if "lalala" in punto:
    print(punto["lalala"])
    
# usar get para saber si un valor esta en el diccionario
print(punto.get("lalala", 100)) # se coloca el valor 100 para que no diga None    

# eliminar valore del diccionario
del punto["x"]
print(punto)
del punto["y"]
print(punto)

# volvemos a agregar el valor x
punto["x"] = 5
print(punto)

# recorrer el diccionario
# for llave in punto:
#     print(llave, punto[llave])
    
for llave in punto.items():
    print(llave)    
    
# desempaquetado usando for
for llave, valor in punto.items():
    print(llave, valor)    
    
usuarios = [
    {"id":1,
     "nombres":"Gustavo", 
     "profesion":"docente"
     },
    {"id":2,
     "nombres":"Johana", 
     "profesion":"enfermera"
     },
    {"id":3,"nombres":"Albana", 
     "profesion":"ama de casa"
     },
    {"id":4,"nombres":"Florencia", 
     "profesion":"estudiante"},
    {"id":5,"nombres":"Ricardo", 
     "profesion":"enfermero"}
]    

for usuario in usuarios:
    print(usuario)

for usuario2 in usuarios:
    print(usuario2["nombres"])

for usuario3 in usuarios:
    print(usuario3["profesion"])   