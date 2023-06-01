from collections import deque

fila = deque([1,2])
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)
# eliminar elementos de la fila // elimina elementos a la izquierda
fila.popleft()
print(fila)
#fila.clear() se pueden eliminar todos los elementos de la fila
if not fila:
    print("fila vacía")
else:
    print("fila con elementos")    