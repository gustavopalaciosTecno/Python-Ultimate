# numero = 1
# while numero < 100:
#     print(numero)   
#     # tambien se puede hacer numero = numero * 2
#     numero *=2
    
    
comando = ""
while comando.lower() != "salir":
    comando = input("$ ")  
    print(comando)
# podemos convertirlo en un loop infinito (bucle infinito)    
comando = ""
while True:
    comando = input("$ ")  
    print(comando) # debemos paralo con Ctrl + C
    
