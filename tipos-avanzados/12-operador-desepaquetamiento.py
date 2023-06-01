# operador de desempaquetamiento

lista = [1,2,3,4]
print(*lista)

otraLista = (1,2,3,4)
print(otraLista)

# combinar listas
combinada = [*lista, *otraLista]
print(combinada)

# operador de desempaquetamiento para diccionarios
primerLista = {"valor1":15}
segundaLista = {"valor2":25}

listasCombinadas = {**primerLista, **segundaLista}
print(listasCombinadas)
