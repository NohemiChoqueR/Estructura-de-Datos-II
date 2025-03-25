from producto import Producto

class Venta:
    """Clase que representa una venta de productos."""
    def __init__(self, producto_comprado, cantidad_comprada):
        """Inicializa una venta con un producto y cantidad."""
        self._producto_comprado = producto_comprado
        self._cantidad_comprada = cantidad_comprada
        self._precio_total = 0.0

    @property
    def producto_comprado(self):
        """Este método devuelve el producto."""
        return self._producto_comprado
    
    @producto_comprado.setter
    def producto_comprado(self, new_prod):
        """Este método establece el producto_comprado.""" 
        self._producto_comprado = new_prod

    @property
    def cantidad_comprada(self):
        """Este método devuelve la cantidad_comprada del producto."""
        return self._cantidad_comprada 
    
    @cantidad_comprada.setter
    def cantidad_comprada(self, cant):
        """Este método establece la cantidad del producto."""
        self._cantidad_comprada = cant 

    @property
    def precio_total(self):
        """Este método devuelve el precio_total."""
        return self._precio_total
    
    @precio_total.setter
    def precio_total(self, prec):
        """Este método establece el precio_total del producto."""
        self._precio_total = prec

    def calcular_precio_total(self):
        """Calcula el precio total de la venta."""
        self._precio_total = self.cantidad_comprada * self.producto_comprado.precio
        return self.precio_total
    
    # Método mostrar_venta
    def mostrar_venta(self):
        """Muestra los detalles de la venta."""
        print("\n**** VENTA DEL PRODUCTO ****")
        print(f"Producto: {self.producto_comprado.nombre_producto}")
        print(f"Cantidad comprada: {self.cantidad_comprada}")
        print(f"Precio total: {self.precio_total}")

def main():
    """Función principal para probar la clase Venta."""
    producto1 = Producto('Martillo', 25, 10)
    print(producto1)
    producto1.nombre_producto = "Martillo de acero"
    producto1.precio = 30 
    producto1.cantidad = 15
    print(producto1)

    # Modificar atributos del producto
    producto1.nombre_producto = "Martillo de acero"
    producto1.precio = 30 
    producto1.cantidad = 15
    print(producto1)

    # Crear y mostrar la venta
    venta = Venta(producto1, 3)
    venta.calcular_precio_total()
    venta.mostrar_venta()

if __name__ == "__main__":
    main()
