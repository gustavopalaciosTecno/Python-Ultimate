numeros = [2,5,8,9,12,15,25,2,2,5,5,5,6,4,1,2,12,25]
numeros.sort()
print(numeros)

# Ordenar los valores pero al reves
numeros.sort(reverse=True)
print(numeros)

numeros2 = sorted(numeros, reverse=True)
print(numeros2)

alumnos = [
    ['Juan',15],
    ['Alberto',18],
    ['Manuela',12],
    ["Elvesia",16]
]

# podemos usar una función para luego llamarla
# def ordena(elemento):
#     return elemento[1]

# aunque mejor es usar la funcón lambda (función anónima)

alumnos.sort(key=lambda elemento:elemento[1])
print(alumnos)

