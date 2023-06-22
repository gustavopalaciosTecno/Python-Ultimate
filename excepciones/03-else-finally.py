try:
    
    n = int(input("Ingresa un valor numérico: "))
    
except Exception as e:
    print("ocurrio un error")    
else:
    print("No ocurrió nungún error")  
finally:
    print("se ejecuta siempre") # esta parte siempre se va a ejecutar    