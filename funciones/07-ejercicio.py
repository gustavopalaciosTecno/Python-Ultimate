# realizar una función que me ejecute un palíndromo
# def sin_espacios(texto):
#     nuevo_texto = ""
#     for char in texto:
#         if char != " ":
#             nuevo_texto += char
#     return nuevo_texto            

# def es_palindromo(texto):
#     texto = sin_espacios(texto)
#     if texto[::-1] == texto:
#         return "Es un palíndromo"
#     else:
#         return "NO es un palíndromo"     
    


# print(es_palindromo("amo la paloma"))
def sin_espacios(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto
            
def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves   
     
def es_palindromo(texto):
    texto = sin_espacios(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()
    
    
print(es_palindromo("amo la paloma"))
print(es_palindromo("hola mundo"))
    

    
        
        
         
