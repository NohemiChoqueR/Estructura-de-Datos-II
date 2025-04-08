from nodo import Nodo


class ArbolBinarioBusqueda:
    """
    Clase que representa un Árbol Binario de Búsqueda (ABB).

    Atributos:
        __raiz: Nodo raíz del árbol.
    """

    def __init__(self):
        """Inicializa un árbol vacío."""
        self.__raiz = None
    
    @property
    def raiz(self):
        """Devuelve la raíz del árbol."""
        return self.__raiz
    
    @raiz.setter
    def raiz(self, nodo):
        """Establece la raíz del árbol.
        
        Argumentos:
            nodo: Nodo que se asignará como raíz.        
        """
        self.__raiz = nodo

    def vacio(self):
        """Verifica si el árbol está vacío.

        Retorna:
            True si el árbol no tiene nodos; False en caso contrario.
        """
        return self.__raiz is None 

    def insertar(self, dato):
        """Inserta un nuevo dato en el árbol binario de búsqueda.

        Argumentos:
            dato: Valor a insertar en el árbol.
        """
        actual = self.__raiz 

        if self.vacio():
            self.__raiz = Nodo(dato)
            return 
        
        else: 
            while True: 
                if dato < actual.data:
                    if actual.left is None:
                        actual.left = Nodo(dato)
                        break 
                    actual = actual.left 
                elif dato > actual.data:
                    if actual.right is None:
                        actual.right = Nodo(dato)
                        break 
                    actual = actual.right  
                else:
                    return

    def es_hoja(self, nodo): 
        """Verifica si el nodo proporcionado es una hoja.

        Argumentos:
            nodo: Nodo a evaluar.

        Retorna:
            True si el nodo no tiene hijos; False en caso contrario.
        """
        if nodo is None: 
            return False 
        return nodo.left is None and nodo.right is None 
    
    def buscarX(self, valor):
        """Busca un valor en el árbol.

        Argumentos:
            valor: Valor a buscar en el árbol.

        Retorna:
            True si el valor está presente; False en caso contrario.
        """
        actual = self.__raiz

        while actual is not None: 
            if valor == actual.data : 
                return True 
            elif valor > actual.data:
                actual = actual.right
            else:
                actual = actual.left
                
        return False
    
    def inOrden(self):
        """Método público que inicia el recorrido inOrden del árbol."""
        self.__inOrden_recursivo(self.__raiz)  

    def __inOrden_recursivo(self, nodo):
        """Recorrido inOrden: izquierda → nodo → derecha.

        Argumentos:
            nodo: Nodo actual del recorrido.
        """
        if nodo is not None:
            self.__inOrden_recursivo(nodo.left)
            print(nodo.data, end = " ")
            self.__inOrden_recursivo(nodo.right)
      
    def postOrden(self):
        """Método público que inicia el recorrido postOrden del árbol."""
        self.__postOrden_recursivo(self.__raiz) 

    def __postOrden_recursivo(self, nodo):
        """Recorrido postOrden: izquierda → derecha → nodo.

        Argumentos:
            nodo: Nodo actual del recorrido.
        """
        if nodo is not None: 
            self.__postOrden_recursivo(nodo.left)
            self.__postOrden_recursivo(nodo.right)
            print(nodo.data, end = " ")
    
    def preOrden(self):
        """Método público que inicia el recorrido preOrden del árbol."""
        self.__preOrden_recursivo(self.__raiz)

    def __preOrden_recursivo(self, nodo):
        """Recorrido preOrden: nodo → izquierda → derecha.

        Argumentos:
            nodo: Nodo actual del recorrido.
        """
        if nodo is not None: 
            print(nodo.data, end = " ")
            self.__preOrden_recursivo(nodo.left)
            self.__preOrden_recursivo(nodo.right)


def main():
    """Función principal para probar la clase ArbolBinarioBusqueda."""
    arbol = ArbolBinarioBusqueda()

    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(70)
    arbol.insertar(20)
    arbol.insertar(40)
    arbol.insertar(60)
    arbol.insertar(80)

    print("¿El árbol está vacío?")
    print(arbol.vacio())  

    print("\nRecorrido inOrden:")
    arbol.inOrden() 

    print("\n¿Existe el valor 60?")
    print(arbol.buscarX(60))  

    print("¿Existe el valor 90?")
    print(arbol.buscarX(90)) 

    print("\n¿Es hoja el nodo con valor 20?")
    nodo_20 = arbol.raiz.left.left  
    print(arbol.es_hoja(nodo_20)) 

    print("\nRecorrido postOrden:")
    arbol.postOrden() 

    print("\n¿Es hoja el nodo con valor 30?")
    nodo_30 = arbol.raiz.left 
    print(arbol.es_hoja(nodo_30))  

    print("\nRecorrido preOrden:")
    arbol.preOrden() 


if __name__ == "__main__":
    main()





            

