from src.models.NodoM import NodoM
from collections import deque


class ArbolMViasPredictivo:
    """
    Árbol M-vías para diccionario predictivo (autocompletado).

    Métodos principales:
      - insertar(key, frequency): añade o actualiza la frecuencia de una palabra.
      - suggestions(prefix, limit): devuelve hasta `limit` sugerencias para el prefijo dado.
      - inorden(): recorre lexicográficamente todas las palabras.
    """

    def __init__(self, M=4):
        NodoM.M = M
        self.raiz = None

    def insertar(self, key, frequency=1):
        """Inserta `key` con frecuencia inicial `frequency`, o actualiza si ya existe."""
        if self.raiz is None:
            self.raiz = NodoM(key, frequency)
            return
        p, parent, idx = self.raiz, None, 0
        while p is not None:
            if not p.isLleno():
                p.insDataInOrden(key, frequency)
                return
            idx = self._hijo_desc(p, key)
            if idx == -1:  # existe y frecuencia actualizada
                return
            parent, p = p, p.getHijo(idx)
        # crear nuevo nodo hoja
        nuevo = NodoM(key, frequency)
        parent.setHijo(idx, nuevo)

    def _hijo_desc(self, nodo, key):
        """Determina índice de hijo a descender según `key`."""
        # recorre data para hallar posición
        for i in range(1, len(nodo.data) + 1):
            if nodo.isUsada(i):
                if key < nodo.getData(i):
                    return i
                if key == nodo.getData(i):
                    return -1
        return len(nodo.data) + 1

    def suggestions(self, prefix, limit=5):
        """
        Devuelve hasta `limit` sugerencias que empiezan con el prefijo, con su frecuencia.
        """
        matches = []

        def _recorrer(nodo):
            if nodo is None:
                return
            used = nodo.cantDatasUsadas()
            for i in range(1, used + 1):
                _recorrer(nodo.getHijo(i))
                key = nodo.getData(i)
                freq = nodo.getFreq(i)
                if key and key.startswith(prefix):
                    matches.append({'palabra': key, 'frecuencia': freq})
            _recorrer(nodo.getHijo(used + 1))

        _recorrer(self.raiz)
        matches.sort(key=lambda d: (-d['frecuencia'], d['palabra']))
        return matches[:limit]


    def inorden(self):
        """Imprime todas las palabras en orden lexicográfico."""

        def _io(n):
            if not n:
                return
            used = n.cantDatasUsadas()
            for i in range(1, used + 1):
                _io(n.getHijo(i))
                print(f"{n.getData(i)}({n.getFreq(i)})", end=" ")
            _io(n.getHijo(used + 1))

        _io(self.raiz)
        print()

    def por_niveles(self):
        """Imprime el árbol por niveles."""
        if not self.raiz:
            print("Árbol vacío")
            return
        cola = deque([(self.raiz, 0)])
        nivel_actual = -1
        while cola:
            nodo, nivel = cola.popleft()
            if nivel != nivel_actual:
                nivel_actual = nivel
                print(f"\nNivel {nivel}:", end=" ")
            print(str(nodo), end=" ")
            for i in range(1, len(nodo.hijo) + 1):
                h = nodo.getHijo(i)
                if h:
                    cola.append((h, nivel + 1))
        print()

    def contiene(self, key):
        """
        Devuelve True si la palabra 'key' está en el árbol, False si no.
        """
        def _buscar(nodo, key):
            if nodo is None:
                return False
            for i in range(1, len(nodo.data) + 1):
                if nodo.isUsada(i):
                    if nodo.getData(i) == key:
                        return True
        # Buscar en hijos
            for i in range(1, len(nodo.hijo) + 1):
                if _buscar(nodo.getHijo(i), key):
                    return True
            return False

        return _buscar(self.raiz, key)
    
    def obtener_frecuencia(self, key):
        """
        Retorna la frecuencia de 'key' si existe, sino retorna 0.
        """
        def _buscar(nodo, key):
            if nodo is None:
                return 0
            for i in range(1, len(nodo.data) + 1):
                if nodo.isUsada(i):
                    if nodo.getData(i) == key:
                        return nodo.getFreq(i)
        # Buscar en hijos
            for i in range(1, len(nodo.hijo) + 1):
                freq = _buscar(nodo.getHijo(i), key)
                if freq:
                    return freq
            return 0

        return _buscar(self.raiz, key)


