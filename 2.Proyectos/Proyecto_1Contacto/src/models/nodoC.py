from src.models.contacto import Contacto

class NodoC:
    def __init__(self, contacto: Contacto):
        self.contacto = contacto
        self.left = None
        self.right = None

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, new_contact):
        self._contact = new_contact

    # Left child
    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node_left):
        self._left = node_left

    # Right child
    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node_right):
        self._right = node_right
