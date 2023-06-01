class Perro: # usamos la pascal case o Upper camel case empieza con ua mayúscula
    # si colocamos miperro tendría que ser MiPerro (estructura camel case)
    def habla(self): # las funciones dejan de llamarse asi y se llaman ahora métodos
        print("Guau")
        
        
mi_perro = Perro()        
# print(type(mi_perro))
mi_perro.habla()
print(isinstance(mi_perro,Perro)) # pregunta si el método es una instancia de la clase Perro
        
    