usuarios = [
    ["Pepito", 45],
    ["Alberto", 54],
    ["Gladis", 12],
    ["Isabel", 56]    
]
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuarios[0])
# print(nombres)        

# comprensión de listas
# elemento1 = [usuario[0] for usuario in usuarios]
# print(elemento1)
# print("\n")

# map
# elemento2 = [usuario[1] for usuario in usuarios]
# print(elemento2)

# filter
# filtrar para que me imprima solo mayores de 50 años
# nombres = [usuario for usuario in usuarios if usuario[1] >= 56]

# filtrar y transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] >= 56]
# print(nombres)

#aplicando map y lambda
# nombres = list(map(lambda usuario: usuario[0], usuarios))
# print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[1] > 50, usuarios))
print(menosUsuarios)