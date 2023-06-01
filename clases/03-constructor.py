class Perro:
    
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def habla(self):
        print(f" {self.nombre}  dice: Guau")
        
mi_perro = Perro("guardian", 45)
mi_perro2 = Perro("Chanchito",26)
# print(mi_perro.nombre)
# print(mi_perro2.nombre)
print(mi_perro.nombre)
print(mi_perro.edad)
print(mi_perro2.nombre)
print(mi_perro2.edad)
mi_perro.habla()
