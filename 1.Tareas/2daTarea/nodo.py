'''
Titulo: Representacion de un Nodo
'''
class Nodo:
    """
    Clase Nodo para un árbol binario de búsqueda (ABB) 
    Atributos: 
        data: Valor almacenado en el nodo. 
        left: Referencia al nodo hijo izquierdo. 
        right: Referencia al nodo hijo derecho.    
    """
    def __init__(self, value):
        """metodo que crea la instancia del Nodo
        Argumentos: 
            value: Valor a almacenar en el nodo. 
        """
        self.__data = value # Ahora guarda un objeto de tipo Producto
        self.__left = None
        self.__right = None
 
    @property
    def data(self):
        '''Este metodo devuelve el valor almacenado en el nodo'''
        return self.__data 
    
    @data.setter
    def data(self, value):
        '''Este metodo establece el valor del nodo.
        argumentos: 
            value: Nuevo valor para el nodo
        '''
        self.__data = value 

    @property
    def left(self):
        '''Este metodo obtiene el nodo hijo izquierdo.

        retorna:
            Referencia al nodo hijo izquierdo o None si no existe.
        ''' 
        return self.__left 
    
    @left.setter 
    def left(self, node):
        """Establece el nodo hijo izquierdo.
        Argumentos: 
            node: Referencia al nuevo nodo hijo izquierdo.
        """
        self.__left = node 

    @property
    def right(self): 
        """Öbtiene el nodo hijo derecho.
        retorna: 
            Referencia al nodo hijo derecho o None si no existe.
        """
        return self.__right 
    @right.setter
    def right(self, node):
        """Metodo que establece el nodo hijo derecho.
        argumentos: 
            node: Referencia al nuevo nodo hijo derecho.
        """
        self.__right = node 

def main(): 
    """Funcion principal para demostrar el uso de la clase Nodo."""
    nodito = Nodo('20')
    nodito.data = '10'
    print(nodito.data)
    print(nodito.__doc__)

if __name__ == "__main__":
    main()
    

