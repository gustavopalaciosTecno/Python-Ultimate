animales = ["jirafa", "león", "cocodrilo", "hiena", "ñu"]

# iterar la lista
for animal in animales:
    print(animal[0])
    
# iterar una lista desempaquetándola
for indice, animal in enumerate(animales):
    print(indice, animal) # valor 0 es el índice y 1 es el valor
