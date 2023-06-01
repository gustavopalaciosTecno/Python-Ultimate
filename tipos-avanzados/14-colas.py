# tambien se conocen como pilas

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila) 
ultimaFila = pila.pop()
print(ultimaFila) 
print(pila)
print(pila[-1]) # acceder al último elemento que queda en la lista
pila.clear()



if not pila:
    print("pila vacía")
    

