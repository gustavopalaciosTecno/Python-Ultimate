import sys
print("el tamaño de palabra que soporta el sistema es: ",sys.maxsize)

# MUTABILIDAD DE VARIABLES
print("\nMutabilidad de variables")
x,y = 1,4
z = x
print(x,y,z) # se toma una nueva variable que es z
z = 7
print(x,y,z)  # se vuelve a reasignar la variable x

lista = [10,5,2]
lista_copia = lista
lista_copia[2] = -20
print(lista, lista_copia)

# TIPOS BOOLEANOS
print("\nTipos de booleanos")
print(bool(True), bool(False))
print(bool(0), bool(0j), bool(''), bool(None), bool(set())) # todos estos valores equivalen a false
print(bool(1), bool(-1), bool('cara'), bool(25), bool(1.18)) # todos estos valores equivalen a true

# objetos evaluados como falsos son None y False
print(bool(None), bool(False))

# valores numéricos tales como:
print(0)
print(0.0)
print(0j)

# objetos vacíos
print(dict())
print(set())
print(range(0))
print("")
print('')
print([])

# OPERACIONES CON BOOLEANOS
print("\nOperaciones con booleanos")
print(bool(True) and bool(True))
print(24 and 82 and 2) # el resultado será 2
print(False and 21) # el resultado será False
print(23 or "casa") # el resultado será 23
print(23 and "casa") # el resultado será casa
print(True and 0 and 90) # el resultado será 0

# CORTOCIRCUITO LÓGICO
print("\nCortocircuito lógico")
print(0 or 24 or 'libro' or x)
print(16 and True and 0 or x)

# si no tuviera el circuito lógico daría un error al imprimir x
# pagina 88 libro Python a fondo




