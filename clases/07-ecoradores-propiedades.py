class Perro:
    
    def __init__(self, nombre):
        print("pasando por el getter")
        self.nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
        
    @nombre.setter    
    def nombre(self, nombre):
        print("pasando por el setter")
        if nombre.strip():
            self.__nombre = nombre
        return             
    
               
perro = Perro("Choclo")
print(perro.nombre)