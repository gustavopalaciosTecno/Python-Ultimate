# se utiliza para iterar una lista de elementos
# también se utilizan para buscar elementos
# también se utilizan para eliminar elementos
# también se utilizan para insertar elementos
# también se utilizan para ordenar lista
# etc
buscar = 7
for numero in range(5): # range es un iterable, tambien lo son las listas y las tuplas
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no se encontró el número buscado, :(")    

for char in "Ultimate Python": # tambien un string es un iterable
    print(char)