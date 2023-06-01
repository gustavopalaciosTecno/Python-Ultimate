# set: significa grupo o conjunto
numeracion = {1,1,1,4,5,5,6,6,6,9,8,7,10}
print(numeracion)

numeracion.add(85)
print(numeracion)
numeracion.remove(10)
print(numeracion)

# imprimir un set con base a una lista
mi_lista = [115,145,897,452,147]
mi_lista = set(mi_lista)
print(mi_lista)

# uniones de set
primero = {10,20,30,40,50,60,70}
segundo = {5,10,15,20,25,30,35,40,45} # si se repiten los elementos de arriba con los de abajo, elimina los de arriba
#print(primero | segundo)

# intersección de elementos del set
print(primero & segundo)

# diferencias entre elementos
print(primero - segundo)

# diferencia simétrica - elimina los duplicados
print(primero ^ segundo) # con alt + 94 sacamos el símbolo

# no podemos acceder a los elementos del set
# si podemos hacer una condicional
if 10 in primero:
    print("si esta el valor 10")
else:
    print("no se encuentra")    
