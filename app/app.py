# from flask import *
from flask import Flask,render_template, request, redirect
from controller import *

app = Flask(__name__)


@app.route('/')
def getIndex():
    title="Index"
    # conexion = probar_Conexion()
    # print (conexion)
    return render_template("index.html",title=title)

@app.route('/contacto')
def dataContacto():
    title="Contacto"
    return render_template("contacto.html",title=title)

@app.route('/perros')
def dataPerros():
    title="Perros"
    return render_template("perros.html",title=title)

@app.route('/gatos')
def dataGatos():
    title="Gatos"
    return render_template("gatos.html",title=title)

@app.route('/nosotros')
def dataNosotros():
    title="Nosotros"
    return render_template("nosotros.html",title=title)

@app.route('/donar')
def dataDonar():
    title="Donar"
    return render_template("donar.html",title=title)

@app.route('/formAdopsion')
def dataForm():
    title="Formulario de adopcion"
    tipoEstados = obtener_TipoEstado()
    tipoAnimales = obtener_TipoAnimales()
    publicados = obtener_AnimalesPublicados()
    # for row in publicados:
    #        print(row)
    return render_template("formAdopcion.html",title=title,tipoEstados=tipoEstados,tipoAnimales=tipoAnimales,publicados=publicados)

@app.route('/transito')
def dataTransito():
    title="Transito"
    perros = obtener_AnimalesEnTransito('PE')
    gatos = obtener_AnimalesEnTransito('GA')
    return render_template("transito.html",title=title,perros= perros,gatos =gatos )


    # Ruta para procesar el formulario
@app.route("/formularioAdopcionGrabar", methods = ['POST'])
def formularioAdopcion_Grabar():
    # Obtener el valor seleccionado del combo box
    tipoanimal = request.form['tipoanimal']
    idAnimales = request.form['idAnimales']
    tipoestado = request.form['tipoestado']
    print('Grabamos la adopcion')
    # Aquí puedes realizar acciones con el valor seleccionado, como consultas adicionales o redireccionamientos
    print  (f"El tipo de animal seleccionado tiene el ID: {idAnimales} {tipoanimal} {tipoestado}")
    return f"El tipo de animal seleccionado tiene el ID: {idAnimales} {tipoanimal} {tipoestado}"

