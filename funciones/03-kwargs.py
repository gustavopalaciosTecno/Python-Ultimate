def get_product(**datos):
    # para acceder a los datos se utiliza
    print(datos["id"], datos["name"], datos["last_name"])
    
    
get_product(id="10", 
            name="gustavo", 
            last_name="Palacios", 
            proffesion="docente")  


def get_products1(**data):
    print(data["id"], data["country"], data["ocuppation"])
    
 
get_products1(id="1",
              country = "Bahamas",
              ocuppation = "mesera"
              )   

def calculoGeneral(**kwargs):
    resultado_s = suma(**kwargs)
    resultado_d = division(**kwargs)
    return resultado_s + resultado_d 
  
def suma(op1, op2,**kwargs):
    return op1 + op2

def division(num, deno, **kwargs):
    return num / deno

resultado = calculoGeneral(op1 = 5, op2=10, num=15, deno=2)
print("el resultado es: ",resultado)
    
    


   