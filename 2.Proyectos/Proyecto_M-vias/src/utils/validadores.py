import re

def es_correo_valido(correo):
    return re.match(r"[^@]+@[^@]+\.[^@]+", correo)

def es_telefono_valido(telefono):
    return telefono.isdigit()
