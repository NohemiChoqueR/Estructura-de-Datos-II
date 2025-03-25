'''
Title: Representacion de Usuario
Autor: Nohemi Choque Ramirez
Date : 25/03/25
Version: v1.0 
'''
import re
#. Clase que representa un usuario
class Usuarioo:
    def __init__(self, nombre_usuario, contraseña, rol):
        ''''método que crea una instancia de la clase Usuarioo'''
        self._nombre_usuario = nombre_usuario 
        self._contraseña = contraseña
        self._rol = rol 
        '''
        Argumentos:
            nombre_usuario(str): Nombre del usuario. 
            contraseña: Contraseña del usuario.
            rol(str): Rol del usuario('ADMI' o 'USUARIO').
        '''
#. Métodos de la clase Usuarioo
#. Métodos getter y setter de la clase Usuarioo.        
    @property
    def nombre_usuario(self): 
        '''Este método devuelve el nombre del usuario.'''
        return self._nombre_usuario
    
    @nombre_usuario.setter
    def nombre_usuario(self, new_nombre):
        '''Este método establece el nombre del usuario, validando que tenga al menos 3 caracteres'''
        if len(new_nombre) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.") 
        self._nombre_usuario = new_usuario

    @property
    def contrasena(self):
        '''Este método devuelve la contrasena del usuario.'''
        return self._contraseña
    
    @contrasena.setter
    def contrasena(self, new_contrasena):
        '''Este método establece una contrasena.'''
        self._contrasena = new_contrasena

    @property
    def rol(self):
        '''Este método devuelve el rol del usuario.'''
        return self._rol
    
    @rol.setter
    def rol(self,rol):
        '''Este método establece el rol del usuario, validando que sea 'ADMI' o 'USUARIO'.'''
        if rol.upper()=="ADMI":
            self._rol= "ADMI"
        else: 
            if rol.upper()=="USUARIO":
                self._rol="USUARIO"
            else:
                raise ValueError("Rola inválido. Debe ser 'ADMI' o 'USUARIO'. ") 
            
    def actualizar_contrasena(self, nueva_contrasena):
        '''Actualiza la contrasena del usuario.'''
        self._contraseña = nueva_contrasena
        print("Contraseña actualizada exitosamente.")

    def validar_mayuscula(self):
        '''Verifica si la contrasena contiene al menos una letra mayúscula.'''
        return any(c.isupper() for c in self.contrasena)
    
    def validar_minuscula(self):
        '''Verifica si la contrasena contiene al menos una letra minuscula.'''
        return any(c.islower() for c in self.contrasena)
    
    def validar_numero(self):
        ''''Verifica si la contrasena contiene al menos un número.'''
        return any(c.isdigit() for c in self.contrasena)
    def validar_caracter_especial(self):
        '''Verifica si la contrasena contiene al menos un caracter especial.'''
        return bool(re.search(r'[\W]',self.contrasena))

    def validar_contrasena(self):
        '''
        Verifica si la contrasena cumple con los requisitos de seguridad.
        Requisitos:
        - Minimo 12 caracteres
        - Al menos una letra mayúscula
        - Al menos una letra minúscula
        - Al menos un número
        - Al menos un carácter especial
        Retorna:
        str: Mensaje indicando si la contraseña es válida o cuál requisito no cumple.
        '''
        if len(self.contrasena) < 12:
            return "La contraseña debe tener al menos 12 caracteres."
        if not self.validar_mayuscula():
            return "La contraseña debe contener al menos una letra mayúscula."
        if not self.validar_minuscula():
            return "La contraseña debe contener al menos una letra minúscula."
        if not self.validar_numero():
            return "La contraseña debe contener al menos un número."
        if not self.validar_caracter_especial():
            return "La contraseña debe contener al menos un carácter especial."
        return "La contraseña es válida."
    
new_usuario=Usuarioo("Juan","Hola1233333333@!","ADMI")
print(new_usuario.validar_contrasena())
new_usuario.actualizar_contrasena("helouN1233$")
print(new_usuario.contrasena)


