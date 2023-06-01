class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f" {self.nombre} dice Guau")       
        
        
mi_perro = Perro("Guardian", 1)
print(Perro.patas) # llamo directamente a la clase