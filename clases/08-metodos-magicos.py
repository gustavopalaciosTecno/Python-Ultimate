class Perro:
    # el método init es un método mágico // comienzan y terminan con dos guiones bajos
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad
        
    def __del__(self):
        print(f" chau perro 😢 {self.nombre}")
                
    def __str__(self):
        return (f" clase perro: {self.nombre}")
    
    def habla(self):
        return (f"el {self.nombre} dice guau !")        


perro = Perro("Chanchito", 1)
del perro