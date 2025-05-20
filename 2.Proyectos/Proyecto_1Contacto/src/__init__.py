import os
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Config
from dotenv import load_dotenv

# Cargar variables del archivo .flaskenv o .env
load_dotenv()  

# Crear una instancia global de SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key =  os.getenv("SECRET_KEY")

    # Inicializar la base de datos con la app
    db.init_app(app)

    # Registrar el blueprint
    from src.controllers.contactos_controller import bp as contactos_bp
    app.register_blueprint(contactos_bp, url_prefix="/contactos")

    # Ruta raíz redirecciona a /contactos
    @app.route("/")
    def redireccion():
        return redirect("/contactos/")

    # Crear las tablas en la base de datos (si no existen)
    with app.app_context():
        from src.models.contacto import Contacto
        db.create_all()

    # ✅ Cargar ABB desde BD dentro del contexto
        from src.controllers.contactos_controller import abb
        for c in Contacto.query.all():
            abb.insertar(c)
    
    
    return app


