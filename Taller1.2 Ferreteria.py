class Factura:
    
    def __init__(self, numero_pieza, descripcion, cantidad, precio_por_articulo):
        self.numero_pieza = numero_pieza
        self.descripcion = descripcion
        self.establecer_cantidad(cantidad)
        self.establecer_precio(precio_por_articulo)
    
    def establecer_numero_pieza(self, numero_pieza):
        self.numero_pieza = numero_pieza
    
    def obtener_numero_pieza(self):
        return self.numero_pieza
    
    def establecer_descripcion(self, descripcion):
        self.descripcion = descripcion
    
    def obtener_descripcion(self):
        return self.descripcion
    
    def establecer_cantidad(self, cantidad):
        if cantidad > 0:
            self.cantidad = cantidad
        else:
            self.cantidad = 0
    
    def obtener_cantidad(self):
        return self.cantidad
    
    def establecer_precio(self, precio_por_articulo):
        if precio_por_articulo > 0:
            self.precio_por_articulo = precio_por_articulo
        else:
            self.precio_por_articulo = 0
    
    def obtener_precio(self):
        return self.precio_por_articulo
    
    def obtener_monto_factura(self):
        return self.cantidad * self.precio_por_articulo

# Instancia de la clase con sus valores
factura_prueba = Factura("002", "Destornillador", 3, 5)

# Información de la factura
print("Número de pieza:", factura_prueba.obtener_numero_pieza())
print("Descripción:", factura_prueba.obtener_descripcion())
print("Cantidad:", factura_prueba.obtener_cantidad())
print("Precio por artículo:", factura_prueba.obtener_precio())
print("Monto de la factura:", factura_prueba.obtener_monto_factura())