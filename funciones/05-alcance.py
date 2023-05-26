saludo = "hola global"

def saludar():
    global saludo
    #saludo = "hola mundo"
   
def saludaChanchito():
    saludar = "te saluda chanchito"    
    print(saludar)
    
saludar()
saludaChanchito()    
print(saludo)