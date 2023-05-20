print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son: suma, resta, multi, div y resta")

opciones = ["suma","resta", "multi", "div", "multiplicacion", "division"]
valores = []
try:
    while opciones != "salir":
        resultado = int(input("Ingresá un número: "))
    
        operacion = input("ingresá una operación: ")
        if operacion == "salir":
            print("Hasta luego")
            break
        numero1 = int(input("Ingresá otro número: "))
    
        if operacion.lower() == "suma":
            resultado += numero1
            
            #print(f"el resultado es: {resultado}")
                 
        elif operacion.lower() == "resta": 
            
            resultado -= numero1            
            #print(f"el resultado es: {resultado}")   
            
        elif operacion.lower() == "division" or operacion.lower() == "div": 
            resultado /= numero1 
            #print(f"el resultado es: {resultado}")     
       
        elif operacion.lower() == "multi":
            resultado *= numero1
            #print(f"el resultado es: {resultado}") 
                    
        print(f"el resultado es: {resultado}")            
except Exception as typeError:
    print("Coloca un valor numérico por favor !!!", typeError)
finally:
    print("FIN DEL PROGRAMA")   
    
        
                       

            
   
    

    

                 

     



                      
          