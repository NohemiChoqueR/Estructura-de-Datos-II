class NodoM:
    """
    Nodo M-vías adaptado para un diccionario predictivo (autocompletado).

    Atributos:
        M (int): Grado del árbol. Número máximo de hijos.
        hijo (list[NodoM|None]): Referencias a los nodos hijos.
        data (list[str]): Claves (palabras) almacenadas en orden.
        freq (list[int]): Frecuencias asociadas a cada clave.
        usada (list[bool]): Banderas indicando posiciones usadas en `data`.
        cantUsadas (int): Contador de posiciones ocupadas.
    """

    M = 4  # Grado del árbol (puedes ajustar según necesidades)

    def __init__(self, key=None, frequency=1):
        # Inicializar estructuras de tamaño M hijos y M-1 datos
        self.hijo = [None] * NodoM.M
        self.data = [""] * (NodoM.M - 1)
        self.freq = [0] * (NodoM.M - 1)
        self.usada = [False] * (NodoM.M - 1)
        self.cantUsadas = 0
        if key is not None:
            self.setData(1, key, frequency)

    def getHijo(self, i):
        if 1 <= i <= len(self.hijo):
            return self.hijo[i - 1]
        return None

    def setHijo(self, i, nodo):
        if 1 <= i <= len(self.hijo):
            self.hijo[i - 1] = nodo

    def getData(self, i):
        if 1 <= i <= len(self.data) and self.usada[i - 1]:
            return self.data[i - 1]
        return None

    def getFreq(self, i):
        if 1 <= i <= len(self.freq) and self.usada[i - 1]:
            return self.freq[i - 1]
        return 0

    def setData(self, i, key, frequency=1):
        """
        Inserta `key` con frecuencia `frequency` en la posición i (1-index).
        Si la posición estaba vacía, incrementa `cantUsadas`, si no, simplemente actualiza.
        """
        if not (1 <= i <= len(self.data)):
            return
        if not self.usada[i - 1]:
            self.cantUsadas += 1
        self.data[i - 1] = key
        self.freq[i - 1] = frequency
        self.usada[i - 1] = True

    def isVacia(self, i):
        return 1 <= i <= len(self.usada) and not self.usada[i - 1]

    def isUsada(self, i):
        return 1 <= i <= len(self.usada) and self.usada[i - 1]

    def cantDatasUsadas(self):
        return self.cantUsadas

    def cantDatasVacias(self):
        return len(self.data) - self.cantUsadas

    def isLleno(self):
        return self.cantDatasUsadas() == len(self.data)

    def exist(self, key):
        """Devuelve True si `key` está almacenada en este nodo."""
        for idx in range(len(self.data)):
            if self.usada[idx] and self.data[idx] == key:
                return True
        return False

    def expand(self, idx):
        """
        Desplaza datos y frecuencias a la derecha desde índice `idx` (0-index)
        para dejar espacio a una nueva entrada.
        """
        for j in range(len(self.data) - 1, idx, -1):
            self.data[j] = self.data[j - 1]
            self.freq[j] = self.freq[j - 1]
            self.usada[j] = self.usada[j - 1]
        # limpiar posición idx
        self.usada[idx] = False

    def insData(self, i, key, frequency=1):
        """Inserta en posición i desplazando si es necesario."""
        if not (1 <= i <= len(self.data)):
            return
        self.expand(i - 1)
        self.setData(i, key, frequency)

    def insDataInOrden(self, key, frequency=1):
        """
        Inserta `key` de forma ordenada. Si existe, suma frecuencia.
        """
        # Encontrar posición de inserción
        n = self.cantDatasUsadas() - 1
        idx = 0
        while idx <= n and key > self.data[idx]:
            idx += 1
        # Si existe, incrementamos su frecuencia
        if idx <= n and key == self.data[idx]:
            self.freq[idx] += frequency
            return
        # Si no hay espacio, no podemos insertar aquí
        if self.isLleno():
            return
        # Insertar desplazando
        self.insData(idx + 1, key, frequency)

    def __str__(self):
        partes = []
        for i in range(len(self.data)):
            if self.usada[i]:
                partes.append(f"{self.data[i]}({self.freq[i]})")
            else:
                partes.append(" ")
        return "[" + " | ".join(partes) + "]"
