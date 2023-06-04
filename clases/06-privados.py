class Persona:
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre # con CTRL + SHIFT + P y elegimos rename symbol para cambiar la propiedad a privado
        self.edad = edad
        
    def habla(self):
        print(f"{self.__nombre} dice guau")
        
    def get_nombre(self): # creamos un método para acceder al valor dentro de la misma clase
         return self.__nombre   
     
    def set_nombre(self, nombre): # usamos este método para cambiar el valor
        self.__nombre = nombre
        
    @classmethod
    def factory(cls):
        return cls ("Jorgelina", 18)
    
persona1 = Persona.factory()
persona1.habla()
# si intento acceder al atributo privado, me saldrá un error // no se puede acceder desde afuera
# print(persona1.__nombre)
print(persona1.get_nombre()) # de esta manera si podemos acceder           
persona1.set_nombre("Martina")
print(persona1.get_nombre())
# acceder por medio de un diccionario // no sería una buena práctica ya que es un método privado
print(persona1.__dict__)
print(persona1._Persona__nombre) # copiamos el resultado en pantalla
