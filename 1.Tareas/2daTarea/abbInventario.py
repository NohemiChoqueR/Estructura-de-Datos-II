"""
Título: Representación de un Árbol Binario de Búsqueda
Autor: Nohemi Choque Ramirez
Descripción: Implementación de un ABB para gestión de inventario de productos.
"""

from producto import Producto
from nodo import Nodo


class ArbolInventario:
    """Clase que representa un árbol binario de búsqueda para productos."""

    def __init__(self):
        """Inicializa un árbol vacío."""
        self.__raiz = None  # Raíz del árbol

    @property
    def raiz(self):
        """Devuelve la raíz del árbol (para recorridos externos)."""
        return self.__raiz

    def vacio(self):
        """Verifica si el árbol está vacío."""
        return self.__raiz is None

    def insertar(self, producto):
        """Inserta un nuevo producto en el árbol (ordenado por nombre).
        
        Argumentos:
            producto (Producto): Producto a insertar en el árbol.
            
        Raises:
            ValueError: Si el producto ya existe en el árbol.
        """
        if self.vacio():
            self.__raiz = Nodo(producto)
        else:
            self.__insertar_recursivo(self.__raiz, producto)

    def __insertar_recursivo(self, nodo_actual, producto):
        """Método auxiliar recursivo para insertar.
        
        Args:
            nodo_actual (Nodo): Nodo actual en la recursión.
            producto (Producto): Producto a insertar.
        """
        if producto.nombre_producto < nodo_actual.data.nombre_producto:
            if nodo_actual.left is None:
                nodo_actual.left = Nodo(producto)
            else:
                self.__insertar_recursivo(nodo_actual.left, producto)
        elif producto.nombre_producto > nodo_actual.data.nombre_producto:
            if nodo_actual.right is None:
                nodo_actual.right = Nodo(producto)
            else:
                self.__insertar_recursivo(nodo_actual.right, producto)
        else:
            raise ValueError("¡El producto ya existe en el inventario!")

    def buscar(self, nombre_producto):
        """Busca un producto por nombre.
        
        Argumentos:
            nombre_producto (str): Nombre del producto a buscar.
            
        Retorna:
            Producto: El producto encontrado o None si no existe.
        """
        return self.__buscar_recursivo(self.__raiz, nombre_producto)

    def __buscar_recursivo(self, nodo_actual, nombre_producto):
        """Método auxiliar recursivo para buscar."""
        if nodo_actual is None:
            return None
        elif nombre_producto == nodo_actual.data.nombre_producto:
            return nodo_actual.data
        elif nombre_producto < nodo_actual.data.nombre_producto:
            return self.__buscar_recursivo(nodo_actual.left, nombre_producto)
        else:
            return self.__buscar_recursivo(nodo_actual.right, nombre_producto)

    def eliminar(self, nombre_producto):
        """Elimina un producto del árbol.
        
        Argumentos:
            nombre_producto (str): Nombre del producto a eliminar.
        """
        self.__raiz = self.__eliminar_recursivo(self.__raiz, nombre_producto)

    def __eliminar_recursivo(self, nodo_actual, nombre_producto):
        """Método auxiliar recursivo para eliminar."""
        if nodo_actual is None:
            return None

        if nombre_producto < nodo_actual.data.nombre_producto:
            nodo_actual.left = self.__eliminar_recursivo(
                nodo_actual.left, nombre_producto)
        elif nombre_producto > nodo_actual.data.nombre_producto:
            nodo_actual.right = self.__eliminar_recursivo(
                nodo_actual.right, nombre_producto)
        else:
            if nodo_actual.left is None:
                return nodo_actual.right
            elif nodo_actual.right is None:
                return nodo_actual.left

            nodo_minimo = self.__encontrar_minimo(nodo_actual.right)
            nodo_actual.data = nodo_minimo.data
            nodo_actual.right = self.__eliminar_recursivo(
                nodo_actual.right, nodo_minimo.data.nombre_producto)

        return nodo_actual

    def __encontrar_minimo(self, nodo):
        """Encuentra el nodo con el valor mínimo (para eliminación).
        
        Argumentos:
            nodo (Nodo): Nodo raíz del subárbol a buscar.
            
        Retorna:
            Nodo: Nodo con el valor mínimo.
        """
        while nodo.left is not None:
            nodo = nodo.left
        return nodo

    def inorden(self):
        """Devuelve una lista de productos en orden ascendente (por nombre).
        
        Retorna:
            list: Lista de productos ordenados.
        """
        productos = []
        self.__inorden_recursivo(self.__raiz, productos)
        return productos

    def __inorden_recursivo(self, nodo, lista):
        """Método auxiliar para recorrido inorden."""
        if nodo is not None:
            self.__inorden_recursivo(nodo.left, lista)
            lista.append(nodo.data)
            self.__inorden_recursivo(nodo.right, lista)


if __name__ == "__main__":
    arbol = ArbolInventario()
    
    # Insertar productos
    arbol.insertar(Producto("Martillo", 25.0, 10))
    arbol.insertar(Producto("Destornillador", 15.0, 20))
    arbol.insertar(Producto("Clavos", 5.0, 100))
    
    # Buscar un producto
    producto = arbol.buscar("Martillo")
    if producto:
        print(f"Encontrado: {producto}")
    else:
        print("No encontrado")
    
    # Mostrar todos los productos ordenados
    print("\nInventario completo (ordenado por nombre):")
    for prod in arbol.inorden():
        print(prod)
    
    # Eliminar un producto
    arbol.eliminar("Clavos")
    print("\nDespués de eliminar 'Clavos':")
    for prod in arbol.inorden():
        print(prod)