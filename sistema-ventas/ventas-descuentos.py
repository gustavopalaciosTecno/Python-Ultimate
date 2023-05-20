import tkinter as tk

class AplicacionVentas:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Ventas")
        
        # Variables de control
        self.producto_var = tk.StringVar()
        self.precio_var = tk.DoubleVar()
        self.cantidad_var = tk.IntVar()
        self.total_var = tk.DoubleVar()
        
        # Inicializar variables
        self.precio_var.set(0.0)
        self.cantidad_var.set(1)
        self.total_var.set(0.0)
        self.descuento_aplicado = False
        
        # Crear widgets
        etiqueta_producto = tk.Label(root, text="Producto:")
        etiqueta_producto.pack()
        entrada_producto = tk.Entry(root, textvariable=self.producto_var)
        entrada_producto.pack()
        
        etiqueta_precio = tk.Label(root, text="Precio:")
        etiqueta_precio.pack()
        entrada_precio = tk.Entry(root, textvariable=self.precio_var)
        entrada_precio.pack()
        
        etiqueta_cantidad = tk.Label(root, text="Cantidad:")
        etiqueta_cantidad.pack()
        entrada_cantidad = tk.Entry(root, textvariable=self.cantidad_var)
        entrada_cantidad.pack()
        
        boton_vender = tk.Button(root, text="Vender", command=self.realizar_venta)
        boton_vender.pack()
        
        etiqueta_total = tk.Label(root, text="Total:")
        etiqueta_total.pack()
        label_total = tk.Label(root, textvariable=self.total_var)
        label_total.pack()
        
    def realizar_venta(self):
        producto = self.producto_var.get()
        precio = self.precio_var.get()
        cantidad = self.cantidad_var.get()
        
        # Calcular total
        total = self.total_var.get() + precio * cantidad
        
        # Aplicar descuento si se superan 10 productos
        if cantidad > 10 and not self.descuento_aplicado:
            total = total * 0.9
            self.descuento_aplicado = True
        
        # Actualizar el total
        self.total_var.set(total)
        
        # Reiniciar las variables de entrada
        self.producto_var.set("")
        self.precio_var.set(0.0)
        self.cantidad_var.set(1)
    
# Crear la ventana principal
root = tk.Tk()

# Inicializar la aplicación
app = AplicacionVentas(root)

# Iniciar el bucle de eventos
root.mainloop()
