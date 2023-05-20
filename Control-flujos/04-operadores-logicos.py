# Operadores lógicos
# AND, OR, NOT

# en la condición and ambos deben ser True para que el resultado sea True
gas = False
encedido = True

if gas and encedido:
    print("Puedes avanzar")
else:
    print("No puedes avanzar")    
    
# en la condición or ambos valores deben ser False para que el resultado sea False
# si uno de ellos es True y el otro es False, el resultado será True
gas = False
encendido = False

if gas or encendido:
    print("avanza")
else:
    print("no avanza")       
    
# not es la negación del opuesto: si niega False, el resultado es True y viceversa

if not gas or encendido:
    print("podes avanzar")     
    
# también se pueden combinar los operadores lógicos
gas = True
encendido = True
edad = 18
"""
es recomedable colocar en paréntesis 
y se evalúa primero lo que esta dentro del paréntesis
"""
if gas and (encendido and edad >= 18): 
    print(f"Podes avanzar, tenes {edad} años")    
    
if not gas and (encendido and edad >= 18): 
    print(f"Podes avanzar")    
    
# todas las operaciones se evaluan de izquierda a derecha
# a no ser que tenga un paréntesis, así primero se evcalúa lo que está 
# dentro del paréntesis y luego el resto     

"""
Las operaciones con circuitos lógicos consiste en que si hay un operadores and
con false y luego otro and pero con True, la evaluación se detiene en false y 
no sigue evaluando lo siguiente para optimizar la operacion y ahorrar memoria
en la computadora. en el or pasa algo diferente, si la primera es False y la siguiente
es True, evalúa la primera y sigue con la segunda. el operador or necesita un solo
False para que su resultado sea True, si en cambio los dos son False, el resultado
será False.
""" 