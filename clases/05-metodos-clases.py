class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    @classmethod
    def factory(cls):
        return cls("Néstor Gustavo", 42)
    
    
persona = Persona.factory()
print(persona.nombre, persona.edad)            

print("######## \n#############")
class Perro:
    
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
     
    @classmethod    # método de clase // nos referimos a la clase misma
    def habla(cls): # se utiliza cls como convención cuando usamos métodos de clase
        return "guau!"
    
    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 2)
    
Perro.habla()
# perro1 = Perro("Chanquito feliz",2)
# perro2 = Perro("Felipe", 3)
perro3 = Perro.factory()
print(perro3.nombre, perro3.edad)            