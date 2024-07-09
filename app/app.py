from flask import *

app = Flask(__name__)


@app.route('/')
def getIndex():
    title="Index"
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
    return render_template("formAdopcion.html",title=title)

@app.route('/transito')
def dataTransito():
    title="Transito"
    return render_template("transito.html",title=title)

