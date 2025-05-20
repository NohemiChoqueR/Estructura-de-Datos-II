# Biblioteca estándar
from flask import Blueprint, render_template, request, redirect, url_for, flash

# Importaciones locales del proyecto (separadas en grupo)
from src import db
from src.models.contacto import Contacto as ModeloContacto
from src.models.ABBC import ArbolContactos
from src.utils.validadores import es_correo_valido, es_telefono_valido
from src.utils.config_cloudinary import subir_imagen

bp = Blueprint("contactos", __name__, url_prefix="/contactos")
abb = ArbolContactos()




@bp.route("/create", methods=["GET", "POST"])
def crear_contacto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]

        if not es_telefono_valido(telefono) or not es_correo_valido(correo):
            flash("Datos inválidos. Verifica el correo o el teléfono.")
            return redirect(url_for("contactos.crear_contacto"))

        #  Subir imagen a Cloudinary
        foto = request.files.get("foto")
        imagen_url = ""

        if foto:
            imagen_url = subir_imagen(foto)

        nuevo = ModeloContacto(
            nombre=nombre,
            telefono=telefono,
            correo=correo,
            imagen_url=imagen_url  # <- se asigna aquí
        )

        try:
            db.session.add(nuevo)
            db.session.commit()
            abb.insertar(nuevo)
            flash("✅ Contacto agregado correctamente.")
        except Exception as e:
            db.session.rollback()
            print("❌ Error al guardar en BD:", e)
            flash("⚠️ Ya existe un contacto con ese nombre.")

        return redirect(url_for("contactos.listar_contactos"))

    return render_template("contactos/create.html")


@bp.route("/")
def listar_contactos():
    print("📋 Contactos en el ABB (inorden):")
    q = request.args.get("q", "").lower()

    if q:
        resultados = [c for c in abb.inorden() if q in c.nombre.lower() or q in c.correo.lower()]
    else:
        resultados = abb.inorden()

    return render_template("contactos/listado.html", contactos=resultados)


@bp.route("/edit/<nombre>", methods=["GET", "POST"])
def editar_contacto(nombre):
    if request.method == "POST":
        nombre_nuevo = request.form.get("nombre")
        telefono = request.form.get("telefono")
        correo = request.form.get("correo")
        foto = request.files.get("foto")


        if not es_telefono_valido(telefono) or not es_correo_valido(correo):
            flash("Datos inválidos. Verifica el correo o el teléfono.")
            return redirect(
                url_for("contactos.editar_contacto", nombre=nombre)
            )

        try:
            contacto_bd = ModeloContacto.query.filter_by(
                nombre=nombre
            ).first()

            if not contacto_bd:
                raise ValueError("Contacto no encontrado en la base de datos.")

            nombre_anterior = contacto_bd.nombre
            contacto_bd.nombre = nombre_nuevo
            contacto_bd.telefono = telefono
            contacto_bd.correo = correo
        #  Subir nueva imagen si se envió
            if foto and foto.filename != "":
                imagen_url = subir_imagen(foto)
                contacto_bd.imagen_url = imagen_url  # Reemplaza la URL antigua

            db.session.commit()

            # Sincronizar el ABB con los cambios
            if nombre_nuevo != nombre_anterior:
                abb.eliminar(nombre_anterior)
                abb.insertar(contacto_bd)
            else:
                abb.actualizar(nombre_anterior, contacto_bd)

            flash("✅ Contacto actualizado correctamente.")
            return redirect(url_for("contactos.listar_contactos"))

        except Exception as e:
            db.session.rollback()
            print("❌ Error al actualizar contacto:", e)
            flash("Ocurrió un error al actualizar el contacto.")
            return redirect(
                url_for("contactos.editar_contacto", nombre=nombre)
            )

    try:
        contacto = abb.buscar(nombre)

        if contacto is None:
            raise ValueError("Contacto no encontrado")

        return render_template(
            "contactos/edit.html",
            contacto=contacto
        )

    except Exception as e:
        print("❌ Error:", e)
        flash(f"Error al cargar el contacto: {str(e)}")
        return redirect(url_for("contactos.listar_contactos"))
    
@bp.route("/delete/<nombre>", methods=["POST"])
def eliminar_contacto(nombre):
    try:
        # Buscar en la base de datos
        contacto_bd = ModeloContacto.query.filter_by(nombre=nombre).first()

        if not contacto_bd:
            flash("⚠️ Contacto no encontrado en la base de datos.")
            return redirect(url_for("contactos.listar_contactos"))

        # Eliminar de la base de datos primero
        db.session.delete(contacto_bd)
        db.session.commit()

        # Luego eliminar del ABB
        abb.eliminar(nombre)

        flash("✅ Contacto eliminado correctamente.")
        return redirect(url_for("contactos.listar_contactos"))

    except Exception as e:
        db.session.rollback()
        print("❌ Error al eliminar contacto:", e)
        flash("Ocurrió un error al intentar eliminar el contacto.")
        return redirect(url_for("contactos.listar_contactos"))
    
@bp.route("/view/<nombre>")
def ver_contacto(nombre):
    contacto = abb.buscar(nombre)
    if contacto is None:
        flash("Contacto no encontrado")
        return redirect(url_for("contactos.listar_contactos"))
    return render_template("contactos/ver.html", contacto=contacto)

