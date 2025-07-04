from flask import Blueprint, request, render_template, flash, redirect, url_for, jsonify 
from src.models.arbolMVias import ArbolMViasPredictivo
from bs4 import BeautifulSoup
import requests

bp = Blueprint("predictivo", __name__, url_prefix="/predictivo")

tree = ArbolMViasPredictivo(M=4)
for w in ["Mars","Mark Twain","Martin Luther King Jr.","Maradona", "wikipedia", "marie curie", "python", "einstein","Algorithm","Algebra","Algeria","Algae","Algebraic geometry","Eintracht Frankfurt"]:
    tree.insertar(w.lower(), frequency=1)

@bp.route("/")
def index():
    return render_template("predictivo1.html",
                           resultado=None,
                           mensaje=None,
                           palabra="",
                           contenido_html="")

@bp.route("/sugerencias")
def sugerencias():
    pref = request.args.get("q", "").strip().lower()   # <-- .lower()
    limit = int(request.args.get("limit", 5))
    return jsonify(tree.suggestions(pref, limit))

@bp.route("/agregar-palabra", methods=["POST"])
def agregar_palabra():
    """Endpoint para agregar una nueva palabra al árbol predictivo"""
    palabra = request.form.get("palabra", "").strip()
    frecuencia = request.form.get("frecuencia", "1").strip()
    
    if not palabra:
        flash("Por favor, ingresa una palabra válida.", "error")
        return redirect(url_for("predictivo.index"))
    
    try:
        frecuencia = int(frecuencia) if frecuencia else 1
        if frecuencia < 1:
            frecuencia = 1
    except ValueError:
        frecuencia = 1
    
    # Verificar si la palabra ya existe
    if tree.contiene(palabra.lower()):
        # Si existe, actualizamos su frecuencia
        freq_actual = tree.obtener_frecuencia(palabra.lower())
        nueva_freq = freq_actual + frecuencia
        tree.insertar(palabra.lower(), nueva_freq)
        flash(f"Palabra '{palabra}' actualizada. Nueva frecuencia: {nueva_freq}", "success")
    else:
        # Si no existe, la insertamos
        tree.insertar(palabra.lower(), frecuencia)
        flash(f"Palabra '{palabra}' agregada exitosamente con frecuencia: {frecuencia}", "success")
    
    return redirect(url_for("predictivo.index"))

@bp.route("/palabras-arbol")
def ver_palabras_arbol():
    """Endpoint para ver todas las palabras en el árbol con sus frecuencias"""
    palabras = []
    
    def _recorrer(nodo):
        if nodo is None:
            return
        used = nodo.cantDatasUsadas()
        for i in range(1, used + 1):
            _recorrer(nodo.getHijo(i))
            key = nodo.getData(i)
            freq = nodo.getFreq(i)
            if key:
                palabras.append({'palabra': key, 'frecuencia': freq})
        _recorrer(nodo.getHijo(used + 1))
    
    _recorrer(tree.raiz)
    palabras.sort(key=lambda x: (-x['frecuencia'], x['palabra']))
    
    return render_template("palabras_arbol.html", palabras=palabras)


@bp.route("/buscar", methods=["GET"])
def buscar():
    palabra = request.args.get("q", "").strip()
    resultado = None
    mensaje = None
    contenido_html = ""
    secciones_a_mostrar = [
        "Biography", "Early life", "Scientific career", "Awards",
        "Premios", "Carrera", "Biografía", "Personal life", "Legacy"
    ]

    if not palabra:
        mensaje = "Por favor, ingresa una palabra para buscar."
        return render_template(
            "predictivo1.html",
            resultado=resultado,
            mensaje=mensaje,
            palabra=palabra,
            contenido_html=contenido_html,
        )

    # Llamada al endpoint summary de Wikipedia
    url_summary = f"https://en.wikipedia.org/api/rest_v1/page/summary/{palabra.replace(' ', '_')}"
    res_sum = requests.get(url_summary)

    if res_sum.status_code == 200:
        data = res_sum.json()
        # Solo procesamos si no es página de desambiguación y hay extract
        if data.get("type") != "disambiguation" and data.get("extract"):
            resultado = {
                "titulo": data.get("title"),
                "descripcion": data.get("description"),
                "resumen": data.get("extract"),
                "imagen": data.get("thumbnail", {}).get("source"),
                "url": data.get("content_urls", {}).get("desktop", {}).get("page"),
            }

            tree.insertar(palabra.lower(), frequency=1)

            page_title = data.get("title", palabra).replace(" ", "_")
            url_action = (
                f"https://en.wikipedia.org/w/api.php"
                f"?action=parse&page={page_title}&format=json&prop=text"
            )
            res_action = requests.get(url_action)
            if res_action.status_code == 200:
                data_action = res_action.json()
                full_html = data_action.get("parse", {}).get("text", {}).get("*", "")
                soup = BeautifulSoup(full_html, "html.parser")

                # Removemos la infobox
                for inf in soup.find_all("table", class_="infobox"):
                    inf.decompose()

                # 1. Agregamos los dos primeros párrafos
                main_content = soup.find('div', {'class': 'mw-parser-output'})
                p_count = 0
                if main_content:
                    for elem in main_content.children:
                        if elem.name == 'p' and elem.get_text(strip=True):
                            contenido_html += str(elem)
                            p_count += 1
                            if p_count >= 2:
                                break

                # 2. Sectiones importantes
                for h in soup.find_all(["h2", "h3"]):
                    sec_title = h.get_text().strip().replace("[edit]", "")
                    if any(sec.lower() in sec_title.lower() for sec in secciones_a_mostrar):
                        contenido_temporal = ""
                        for sib in h.find_next_siblings():
                            if sib.name and sib.name in ["h2", "h3"]:
                                break
                            if sib.name in ['p', 'ul', 'ol'] and sib.get_text(strip=True):
                                contenido_temporal += str(sib)
                        if contenido_temporal:
                            contenido_html += str(h) + contenido_temporal

                # 3. Si no hay contenido específico, mostramos todo el HTML principal
                if not contenido_html and main_content:
                    contenido_html = ''.join(
                        str(x) for x in main_content.find_all(['p', 'ul', 'ol'], recursive=False)
                    )
        else:
            mensaje = "No se encontró información clara para esta búsqueda."
    else:
        mensaje = "No se pudo consultar Wikipedia."

    return render_template(
        "predictivo1.html",
        resultado=resultado,
        mensaje=mensaje,
        palabra=palabra,
        contenido_html=contenido_html,
    )
