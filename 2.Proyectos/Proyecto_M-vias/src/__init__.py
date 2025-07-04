import os
from flask import Flask, redirect
from dotenv import load_dotenv

# Carga de variables de entorno (opcional si usas SECRET_KEY)
load_dotenv()


def create_app():
    # Indica explícitamente dónde están tus carpetas de templates y static
    app = Flask(
        __name__,
        template_folder="templates",   # apunta a src/templates
        static_folder="static"         # apunta a src/static
    )

    app.secret_key = os.getenv("SECRET_KEY", "dev-key")

    from src.controllers.predictivo_controller import bp as predictivo_bp
    app.register_blueprint(predictivo_bp)     # monta en /predictivo

    @app.route("/")
    def home():
        return redirect("/predictivo/")

    return app



