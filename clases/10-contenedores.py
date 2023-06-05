class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
       return (f"Nombre: {self.nombre} -  Precio: {self.precio}")        
    
class Categoria:    
    productos = []
    
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
        
    def agregar(self, producto):
        self.productos.append(producto)
        
    def imprimir(self):
        for producto in self.productos:
            print(producto)
 
bicicleta = Producto("bicicleta mountain bike", 15000) 
mochila = Producto("mochila impermeable", 800)       
deportes = Categoria("deportes", [bicicleta, mochila])
deportes.agregar(bicicleta)
deportes.imprimir()
               