from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from database import db
import hashlib
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/")
@app.route("/inicio")
def inicio():
    actividades = db.get_last_actividades(5) 
    return render_template('inicio/index.html', actividades=actividades)

@app.route("/ver_list_act")
def ver_list_act():
   
    pass

@app.route('/agregar_act', methods=["GET", "POST"])
def agregar():
    error = None
    mensaje = None
    if request.method == "POST":
        valido, errores = validar_formulario(request)
        if not valido:
            error = errores
        else:
            insertar_tablas(request)   
            mensaje = "Agregado correctamente"
    return render_template("auth/agregar_act.html", mensaje=mensaje, error=error)

@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    return render_template("auth/estadisticas.html")

def insertar_tablas(req):
    region = req.form.get('region')
    comuna = req.form.get('comuna')
    sector = req.form.get('sector', '')
    nombre = req.form.get('nombre')
    email = req.form.get('email')
    telefono = req.form.get('telefono', '')
    contactar_por = req.form.get('contactar_por', '')
    contacto_id = req.form.get('contacto_id', '')
    fecha_inicio = req.form.get('inicio')
    fecha_termino = req.form.get('termino')
    tema = req.form.get('tema')
    otro_tema = req.form.get('otro_tema', '')
    descripcion = req.form.get('descripcion')
    fotos = req.files.getlist('fotos[]')
    print("Comuna recibida:", comuna)
    comuna_id = db.get_comuna_by_name(comuna).id

    actividad_id = db.create_actividad(comuna_id, sector, nombre, email, telefono, fecha_inicio, fecha_termino, descripcion)
    db.create_ActividadTema(tema, otro_tema, actividad_id)
    db.create_ContactarPor(contactar_por, contacto_id, actividad_id)
    for foto in fotos:
        if foto and foto.filename != '':
            filename = secure_filename(foto.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            foto.save(save_path)

            # URL relativa para acceder desde el navegador
            url = f"/{app.config['UPLOAD_FOLDER']}/{filename}"

            # Guarda en la base de datos
            db.create_foto(url, filename, actividad_id)

if __name__ == '__main__':
    app.run(debug=False)