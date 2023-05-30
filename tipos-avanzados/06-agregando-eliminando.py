animales = [
    "jirafa", 
    "león", 
    "cocodrilo", 
    "hiena", 
    "ñu", 
    "jirafa"
    ]

animales.insert(1,"comadreja")
print(animales)
animales.remove("hiena")
print(animales)
animales.pop() # me borra el último elemento
print(animales)
animales.append("chanchito feliz") # agrega un valor al último de la lista
print(animales)
del animales[3]
print(animales)
animales.clear() # limpiar la lista
print(animales)