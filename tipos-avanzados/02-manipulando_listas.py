mascotas = ["pelusa", "copito", "firulais", "masita", "bellota"]
mascotas[3]="narizita"
print(mascotas[:])
print(mascotas[2:4])
print(mascotas[::2])

# mostrar impares manipulando listas
numeros = list(range(21))
print("valores impares",numeros[1::2])

# mostrar pares manipulando listas
numeros = list(range(21))
print("valores pares",numeros[::2])

# mostrar pares manipulando listas sin el cero
numeros = list(range(1,20))
print("valores pares",numeros[1::2])