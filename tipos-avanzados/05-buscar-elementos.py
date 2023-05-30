# animales = ["jirafa", "león", "cocodrilo", "hiena", "ñu", "jirafa"]

# print(animales.count("jirafa"))
# if "cocodrilo" in animales:
#     print(animales.index("cocodrilo"))  

def valor_buscado(lista, valor):
    for elemento in lista:
        if elemento == valor:
            return "elemento encontrado"
        
    return "elemento no encontrado"


mi_lista = ["mapuche", "comechingones", "toba", "guaraní"]
buscar = input("coloca el nombre a buscar: ")
resultado = valor_buscado(mi_lista, buscar)
print(resultado)
    
    