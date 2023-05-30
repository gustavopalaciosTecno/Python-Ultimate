numeros = [1,2,3,4,5,6,7,8,9]

# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)


# imprimir solo un elemento
# primero, *otros = numeros
# print(primero)

# mostrar el primero y el segundo elemento
primero, *otros, ultimo = numeros
print(primero, ultimo, otros)