import tkinter as tk

class AplicacionComprasVentas:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Compras y Ventas")
        
        # Variables de control
        self.producto_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        
        # Crear widgets
        etiqueta_producto = tk.Label(root, text="Producto:")
        etiqueta_producto.pack()
        entrada_producto = tk.Entry(root, textvariable=self.producto_var)
        entrada_producto.pack()
        
        etiqueta_precio = tk.Label(root, text="Precio:")
        etiqueta_precio.pack()
        entrada_precio = tk.Entry(root, textvariable=self.precio_var)
        entrada_precio.pack()
        
        boton_comprar = tk.Button(root, text="Comprar", command=self.comprar_producto)
        boton_comprar.pack()
        
        boton_vender = tk.Button(root, text="Vender", command=self.vender_producto)
        boton_vender.pack()
        
        self.lista_productos = tk.Listbox(root)
        self.lista_productos.pack()
        
    def comprar_producto(self):
        producto = self.producto_var.get()
        precio = self.precio_var.get()
        self.lista_productos.insert(tk.END, f"Comprado: {producto} - Precio: {precio}")
    
    def vender_producto(self):
        producto = self.producto_var.get()
        precio = self.precio_var.get()
        self.lista_productos.insert(tk.END, f"Vendido: {producto} - Precio: {precio}")
    
# Crear la ventana principal
root = tk.Tk()

# Inicializar la aplicación
app = AplicacionComprasVentas(root)

# Iniciar el bucle de eventos
root.mainloop()
