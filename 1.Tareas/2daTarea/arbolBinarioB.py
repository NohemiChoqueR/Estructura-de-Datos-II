from nodo import Nodo
"""
Titulo: Representacion de un Arbol Binario de Busqueda (ABB) como ADT. 
Autor: Nohemi Choque Ramirez.
Fecha: 02/04/25
"""

class ArbolBinarioBusqueda:
    """Implementación de un Árbol Binario de Búsqueda (ABB).

    Atributos:
        raiz: Referencia al nodo raíz del árbol
    """

    def __init__(self):
        """Inicializa un árbol binario de búsqueda vacío."""
        self.raiz = None

    def vacio(self):
        """método que verifica si el árbol está vacío.

        Returns:
            bool: True si el árbol está vacío, False si no lo esta
        """
        return self.raiz is None

    def insertar(self, dato):
        """Inserta un nuevo dato en el árbol, utiliza un metodo auxiliar recursivo
        en caso el árbol no este vacío.

        Argumentos:
            dato: Valor a insertar en el árbol
        """
        if self.vacio():
            self.raiz = Nodo(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)


    def insertar_iterativo(self, dato):
        """Inserta un dato en el árbol de forma iterativa.
    
        Argumentos:
            dato: El valor a insertar en el árbol.
        """
        if self.vacio():
            self.raiz = Nodo(dato)
            return 
        
        actual = self.raiz 
        while True: 
            if dato < actual.data:
                if actual.left is None: 
                    actual.left = Nodo(dato)
                    break 
                actual = actual.left 
            else:
                if actual.right is None: 
                    actual.right = Nodo(dato)
                    break
                actual = actual.right


    def _insertar_recursivo(self, nodo_actual, dato):
        """Método auxiliar para inserción recursiva.
        Argumentos:
            nodo_actual: Nodo actual en la recursión
            dato: Valor a insertar
        """
        if dato < nodo_actual.data:
            if nodo_actual.left is None:
                nodo_actual.left = Nodo(dato)
            else:
                self._insertar_recursivo(nodo_actual.left, dato)
        elif dato > nodo_actual.data:
            if nodo_actual.right is None:
                nodo_actual.right = Nodo(dato)
            else:
                self._insertar_recursivo(nodo_actual.right, dato)

    def buscar(self, dato):
        """Busca un dato en el árbol.
        Argumentos:
            dato: Valor a buscar
        Retorna:
            bool: True si el dato está en el árbol, False en caso contrario
        """
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo_actual, dato):
        """Método auxiliar para búsqueda recursiva.

        Argumentos:
            nodo_actual: Nodo actual en la recursión
            dato: Valor a buscar

        Returns:
            bool: True si el dato está en el subárbol, False si no lo esta
        """
        if nodo_actual is None:
            return False
        if dato == nodo_actual.data:
            return True
        if dato < nodo_actual.data:
            return self._buscar_recursivo(nodo_actual.left, dato)
        return self._buscar_recursivo(nodo_actual.right, dato)
    

    def buscar_iterativo(self, dato):
        """Busca un dato en el árbol de forma iterativa.
    
        Argumentos:
            dato: Valor a buscar en el árbol.
        
        Retorna:
            bool: True si el dato existe, False si no se encuentra.
        """
        actual = self.raiz
    
        while actual is not None:
            if dato == actual.data:
                return True
            elif dato < actual.data:
                actual = actual.left
            else:
                actual = actual.right
    
        return False

    def eliminar(self, dato):
        """Metodo que elimina un dato del árbol.

        Argumentos:
            dato: Valor a eliminar
        """
        self.raiz = self._eliminar_recursivo(self.raiz, dato)

    def _eliminar_recursivo(self, nodo_actual, dato):
        """Método auxiliar para eliminación recursiva.
        Argumentos:
            nodo_actual: Nodo actual en la recursión
            dato: Valor a eliminar

        Returns:
            Nodo: El nodo modificado después de la eliminación
        """
        if nodo_actual is None:
            return None

        if dato < nodo_actual.data:
            nodo_actual.left = self._eliminar_recursivo(
                nodo_actual.left, dato)
        elif dato > nodo_actual.data:
            nodo_actual.right = self._eliminar_recursivo(
                nodo_actual.right, dato)
        else:
            # Nodo con un solo hijo o sin hijos
            if nodo_actual.left is None:
                return nodo_actual.right
            if nodo_actual.right is None:
                return nodo_actual.left

            # Nodo con dos hijos: obtener el sucesor inorden (mínimo en subárbol derecho)
            nodo_actual.data = self._min_valor(nodo_actual.right)
            nodo_actual.right = self._eliminar_recursivo(
                nodo_actual.right, nodo_actual.data)

        return nodo_actual

    def _min_valor(self, nodo):
        """Encuentra el valor mínimo en un subárbol.

        Argumentos:
            nodo: Nodo raíz del subárbol

        Retorna:
            El valor mínimo encontrado
        """
        while nodo.left is not None:
            nodo = nodo.left
        return nodo.data

    def inorden(self):
        """Recorrido inorden del árbol.

        Retorna:
            list: Lista con los elementos en orden inorden
        """
        elementos = []
        self._inorden_recursivo(self.raiz, elementos)
        return elementos

    def _inorden_recursivo(self, nodo, elementos):
        """Método auxiliar para recorrido inorden recursivo.

        Argumentos:
            nodo: Nodo actual en la recursión
            elementos: Lista para almacenar los elementos
        """
        if nodo is not None:
            self._inorden_recursivo(nodo.left, elementos)
            elementos.append(nodo.data)
            self._inorden_recursivo(nodo.right, elementos)


def main():
    """Función principal para demostrar el uso del ABB."""
    arbol = ArbolBinarioBusqueda()
    datos = [50, 30, 70, 20, 40, 60, 80]

    for dato in datos:
        arbol.insertar_iterativo(dato)

    print("Recorrido inorden:", arbol.inorden())
    print("Existe 40?:", arbol.buscar_iterativo(40))
    print("Existe 100?:", arbol.buscar_iterativo(100))

    arbol.eliminar(20)
    print("Recorrido inorden después de eliminar 20:", arbol.inorden())


if __name__ == "__main__":
    main()