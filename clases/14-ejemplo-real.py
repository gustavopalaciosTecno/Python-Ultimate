from abc import ABC, abstractmethod

class Model(ABC):
      
    @property
    @abstractmethod        
    def tabla(self):
        pass
         
    @abstractmethod        
    def guardar(self):
        pass
       
     
    @classmethod    
    def buscar_por_id(self, _id):
        print(f"buscando por {_id} en la tabla {self.tabla}")    
        
class Usuario(Model):
    tabla = "usuario"
    
    def guardar(self):
        print(f"guardando {self.tabla}")
    
    
usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)