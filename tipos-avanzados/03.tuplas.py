numeros = (1,2,3,5,4,5,5,5)
otrosNumeros = (10,10,15,12,16,18,21,100)
valores = numeros + otrosNumeros
print(valores)

# otra forma de sumar tuplas
valores1 = (14,15,19,54,45) + (44,78,45,98,50)
print(valores1)

# convertir lista a tupla
mi_lista = ["verde", "rojo", "azul", "amarillo"]
tupla_nueva = tuple(mi_lista)
print(type(tupla_nueva))
print(tupla_nueva)
# desempaquetar tuplas
primero, segundo, * otros = numeros
print(primero, segundo)

# recorrer tuplas
mi_tupla = ("elefante", "león", "tigre", "leopardo")
for tupla in mi_tupla:
    print(tupla)
    
# en las tuplas no existe el append ni el insert (no se pueden modificar los valores)    