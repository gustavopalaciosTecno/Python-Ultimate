def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado
    
print("vaca feliz") # este es mi breakpoint   
l = largo("hola")    
print(f"la palabra hola tiene una longitud de {l}")