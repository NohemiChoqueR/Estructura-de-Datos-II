from src import db


class Contacto(db.Model):
    """
    Modelo de base de datos para representar un contacto con
    nombre, teléfono y correo electrónico.
    """

    __tablename__ = "contacto"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(120), nullable=False)
    imagen_url = db.Column(db.String(255)) 
    
    def __repr__(self):
        return f"<Contacto {self.nombre}>"
