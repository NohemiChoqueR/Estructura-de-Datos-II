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

    # Opcional: si quieres usar una SECRET_KEY para sesiones, CSRF, etc.
    app.secret_key = os.getenv("SECRET_KEY", "dev-key")

    # ------------------------------------------------------------------
    # 1) Registra sólo tu blueprint de Autocompletado Predictivo
    # ------------------------------------------------------------------
    from src.controllers.predictivo_controller import bp as predictivo_bp
    app.register_blueprint(predictivo_bp)     # monta en /predictivo

    # ------------------------------------------------------------------
    # 2) Redirección de la raíz al autocompletado
    # ------------------------------------------------------------------
    @app.route("/")
    def home():
        return redirect("/predictivo/")

    return app



