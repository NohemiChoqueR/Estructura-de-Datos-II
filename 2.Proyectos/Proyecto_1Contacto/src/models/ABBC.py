from src.models.nodoC import NodoC
from src.models.contacto import Contacto

class ArbolContactos:
    def __init__(self):
        self.raiz = None

    def insertar(self, contacto: Contacto):
        """Inserta un contacto en el árbol ordenado por nombre."""
        if self.buscar(contacto.nombre):
            print(f"⚠️ Ya existe un contacto con el nombre: {contacto.nombre}")
            return
        nuevo_nodo = NodoC(contacto)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, actual: NodoC, nuevo: NodoC):
        if nuevo.contacto.nombre.lower() < actual.contacto.nombre.lower():
            if actual.left is None:
                actual.left = nuevo
            else:
                self._insertar_recursivo(actual.left, nuevo)
        else:
            if actual.right is None:
                actual.right = nuevo
            else:
                self._insertar_recursivo(actual.right, nuevo)

    def inorden(self):
        """Retorna una lista de contactos ordenados alfabéticamente."""
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo: NodoC, resultado: list):
        if nodo:
            self._inorden_recursivo(nodo.left, resultado)
            resultado.append(nodo.contacto)
            self._inorden_recursivo(nodo.right, resultado)

    def buscar(self, nombre: str):
        """Busca un contacto por nombre exacto."""
        return self._buscar_recursivo(self.raiz, nombre.lower())

    def _buscar_recursivo(self, nodo: NodoC, nombre: str):
        if nodo is None:
            return None
        if nombre == nodo.contacto.nombre.lower():
            return nodo.contacto
        elif nombre < nodo.contacto.nombre.lower():
            return self._buscar_recursivo(nodo.left, nombre)
        else:
            return self._buscar_recursivo(nodo.right, nombre)
        

    def eliminar(self, nombre: str):
        self.raiz = self._eliminar_recursivo(self.raiz, nombre.lower())

    def _eliminar_recursivo(self, nodo, nombre):
        if nodo is None:
            return None

        if nombre < nodo.contacto.nombre.lower():
            nodo.left = self._eliminar_recursivo(nodo.left, nombre)
        elif nombre > nodo.contacto.nombre.lower():
            nodo.right = self._eliminar_recursivo(nodo.right, nombre)
        else:
            if nodo.left is None and nodo.right is None:
                return None
        # Nodo encontrado
            if nodo.left is None:
                return nodo.right
            elif nodo.right is None:
                return nodo.left

        # Caso con dos hijos
            sucesor = self._minimo(nodo.right)
            nodo.contacto = sucesor.contacto
            nodo.right = self._eliminar_recursivo(nodo.right, sucesor.contacto.nombre.lower())

        return nodo

    def _minimo(self, nodo):
        while nodo.left is not None:
            nodo = nodo.left
        return nodo
    
    def actualizar(self, nombre: str, nuevo_contacto: Contacto):
        """
        Actualiza el teléfono y correo de un contacto existente.

        Parámetros:
            nombre (str): Nombre del contacto a buscar (clave del árbol).
            nuevo_contacto (Contacto): Objeto con los nuevos datos.

        Lanza:
            ValueError: Si no se encuentra el contacto.
        """
        nodo = self._buscar_nodo(self.raiz, nombre.lower())
        if nodo is None:
            raise ValueError(f"Contacto '{nombre}' no encontrado")

        nodo.contacto.telefono = nuevo_contacto.telefono
        nodo.contacto.correo = nuevo_contacto.correo
        nodo.contacto.imagen_url = nuevo_contacto.imagen_url

    def _buscar_nodo(self, nodo: NodoC, nombre: str):
        """
        Busca y retorna el nodo que contiene al contacto con el nombre dado.

        Parámetros:
            nodo (NodoC): Nodo actual del recorrido.
            nombre (str): Nombre a buscar.

        Retorna:
            NodoC o None: El nodo si lo encuentra, None si no existe.
        """
        if nodo is None:
            return None
        if nombre == nodo.contacto.nombre.lower():
            return nodo
        elif nombre < nodo.contacto.nombre.lower():
            return self._buscar_nodo(nodo.left, nombre)
        else:
            return self._buscar_nodo(nodo.right, nombre)
        
    def editar_nombre(arbol, nombre_actual, nuevo_contacto):
        """
        Edita el nombre de un contacto eliminando el actual e insertando el nuevo.

        :param arbol: Instancia de ArbolContactos.
        :param nombre_actual: Nombre del contacto existente.
        :param nuevo_contacto: Objeto Contacto con el nuevo nombre y datos.
        """
        contacto_existente = arbol.buscar(nombre_actual)
        if contacto_existente is None:
            raise ValueError("El contacto a editar no existe")

        # Eliminar el nodo con el nombre actual
        arbol.eliminar(nombre_actual)

        # Insertar el nuevo contacto (con nuevo nombre)
        arbol.insertar(nuevo_contacto)


