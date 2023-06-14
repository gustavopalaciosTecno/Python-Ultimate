class Animal:
  def comer(self):
    print("comiendo")

class Perro(Animal):
    def pasear(self):
        print("paseando")
        
          
class Chanchito(Perro): # Herencia mutinivel
    def comer(self):
        print("comiendo")
        
    def programar(self):
        print("programando")                        

chanchito = Chanchito()
chanchito.comer()        