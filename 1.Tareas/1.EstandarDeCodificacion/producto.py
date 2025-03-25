'''
Title: Representacion de Producto
Autor: Nohemi Choque Ramirez
Date : 25/03/25
Version: v1.0 
'''
#. Clase que representa un Producto
class Producto: 
    def __init__(self, nombre, precio, cantidad):
        """método que crea una instancia de la clase Producto."""
        self._nombre_producto = nombre
        self._precio = precio 
        self._cantidad = cantidad
        """
        Argumentos:
            nombre(str): Nombre del producto. 
            precio(float): Precio del producto. 
            cantidad(int): Cantidad del producto.
        """ 
#. Métodos getter y setter de la clase Producto. 
    @property
    def nombre_producto(self):
        """Este método devuelve el nombre del producto."""
        return self._nombre_producto 
    
    @nombre_producto.setter
    def nombre_producto(self, nombre):
        """Este método establece el nombre del producto."""
        self._nombre_producto = nombre 

    @property
    def precio(self):
        """Este método devuelve el precio del producto."""
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        """Este método establece el precio del producto.""" 
        if nuevo_precio >= 0:
            self._precio = nuevo_precio 
        else: 
            raise ValueError("El precio no puede ser negativo")
        
    @property
    def cantidad(self):
        """Este método devuelve la cantidad del producto."""
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cant):
        """Este método establece la cantidad del producto.""" 
        if cant >= 0: 
            self._cantidad = cant
        else: 
            raise ValueError("La cantidad no puede ser negativa.") 
#. Métodos de la clase Producto
    def aumentar_cantidad(self, cantidad_recibida):
        """Este método incrementa la cantidad cuando se reciben productos."""
        if cantidad_recibida > 0: 
            self._cantidad += cantidad_recibida
        else:
            raise ValueError("La cantidad no puede ser negativa.")

    def reducir_cantidad(self, cantidad_vendida):
        """Este método reduce la cantidad del inventario tras una venta."""      
        if cantidad_vendida > self.cantidad: 
            raise ValueError("No hay suficiente stock disponible.")
        if cantidad_vendida < 0:
            raise ValueError("La cantidad recibida no puede ser negativa")
        
        self._cantidad -= cantidad_vendida

    def __str__(self):
        return (f"Producto: {self._nombre_producto},"
                f"Precio: ${self._precio:.2f}, " 
                f"Cantidad: {self._cantidad}")

def main():
    producto = Producto("Martillo", 25, 10)
    print(producto)

    producto.nombre_producto = "Martillo de acero"
    producto.precio = 30
    producto.cantidad = 15
    print(producto)

    producto.reducir_cantidad(3)
    print(f"Despues de venta: {producto}")

    producto.aumentar_cantidad(5)
    print(f"Despues de reposicion: {producto}")

if __name__ == "__main__":
    main()