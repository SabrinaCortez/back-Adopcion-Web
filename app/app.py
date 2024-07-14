from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from controller import *

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave secreta segura

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'adopcion'

mysql = MySQL(app)
bcrypt = Bcrypt(app)

@app.route('/')
def getIndex():
    title = "Index"
    return render_template("index.html", title=title)

@app.route('/contacto')
def dataContacto():
    title = "Contacto"
    return render_template("contacto.html", title=title)

@app.route('/login', methods=['GET', 'POST'])
def dataLogin():
    title = "Login"
    if request.method == 'POST' and 'usuario' in request.form and 'contrasena' in request.form:
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM usuario WHERE usuario = %s', (usuario,))
        user = cursor.fetchone()
        
        if user and bcrypt.check_password_hash(user[2], contrasena):  # user[2] asumiendo que la contraseña está en el tercer campo
            session['loggedin'] = True
            session['id'] = user[0]  # user[0] asumiendo que el ID está en el primer campo
            session['usuario'] = user[1]  # user[1] asumiendo que el usuario está en el segundo campo
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('getIndex'))
        else:
            flash('Nombre de usuario/contraseña incorrectos', 'danger')
        cursor.close()
    return render_template('login.html', title=title)

@app.route('/registrarte', methods=['GET', 'POST'])
def dataRegistrarte():
    if request.method == 'POST' and 'usuario' in request.form and 'contrasena' in request.form and 'email' in request.form:
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        email = request.form['email']
        
        # Encriptar la contraseña
        hashed_password = bcrypt.generate_password_hash(contrasena).decode('utf-8')
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO usuario (usuario, contrasena, email) VALUES (%s, %s, %s)', (usuario, hashed_password, email))
        mysql.connection.commit()
        cursor.close()
        flash('Te has registrado correctamente', 'success')
        return redirect(url_for('dataLogin'))
    title = "Registrarte"
    return render_template('registrarte.html', title=title)

@app.route('/perros')
def dataPerros():
    title = "Perros"
    perros = obtener_AnimalesPublicados('PE')
    return render_template("perros.html", title=title, perros=perros)

@app.route('/gatos')
def dataGatos():
    title = "Gatos"
    gatos = obtener_AnimalesPublicados('GA')
    return render_template("gatos.html", title=title, gatos=gatos)

@app.route('/nosotros')
def dataNosotros():
    title = "Nosotros"
    return render_template("nosotros.html", title=title)

@app.route('/donar')
def dataDonar():
    title = "Donar"
    return render_template("donar.html", title=title)

@app.route('/formAdopsion')
def dataForm():
    title="Formulario de adopcion"
    tipoEstados = obtener_TipoEstado()
    tipoAnimales = obtener_TipoAnimales()
    publicados = obtener_AnimalesPublicadosNombres()
    # for row in publicados:
    #        print(row)
    return render_template("formAdopcion.html",title=title,tipoEstados=tipoEstados,tipoAnimales=tipoAnimales,publicados=publicados)

@app.route('/transito')
def dataTransito():
    title="Transito"
    perros = obtener_AnimalesEnTransito('PE')
    gatos = obtener_AnimalesEnTransito('GA')
    return render_template("transito.html",title=title,perros=perros,gatos=gatos )

@app.route('/listadoadoptantes')
def Adoptantes_Listado():
    title="Listado Adoptantes"
    adoptantes = adoptante_solicitudes()
    return render_template("listadoAdoptantes.html",title=title,adoptantes=adoptantes)

@app.route('/adoptante_Confirmar/<string:cDNI>/<int:idAnimales>')
def adoptante_Confirmar(cDNI,idAnimales):
    adoptante_confirmar (cDNI, idAnimales )
    return redirect("/listadoadoptantes")

    
@app.route('/adoptante_Anular/<string:cDNI>/<int:idAnimales>')
def adoptante_Anular(cDNI,idAnimales):
    adoptante_negar(cDNI, idAnimales )
    print(cDNI)
    print(idAnimales)
    return redirect("/listadoadoptantes")


    # Ruta para procesar el formulario
@app.route('/formularioAdopcionGrabar', methods = ['POST'])
def formularioAdopcion_Grabar():
    # Obtener el valor seleccionado del combo box
    tipoanimal = request.form['tipoanimal']
    idAnimales = request.form['idAnimales']
    tipoestado = request.form['tipoestado']
    cNombreyApellido = request.form['cNombreyApellido']
    cDNI = request.form['cDNI']
    cCorreo = request.form['cCorreo']
    cLinkInstagram = request.form.get('cTelefono')
    cTelefono = request.form.get('cTelefono')
    dFechaNacimiento = request.form.get('dFechaNacimiento ')
    cCasaDepartamento = request.form.get('cCasaDepartamento')
    print('Grabamos la adopcion')
    adoptante_nuevo(cDNI,cNombreyApellido,cCorreo,cLinkInstagram,cTelefono,dFechaNacimiento,cCasaDepartamento)
    estado_Actualizar (idAnimales , cDNI,tipoestado)
    print  (f"El tipo de animal seleccionado tiene el ID:  {cCasaDepartamento}{dFechaNacimiento} {cTelefono}{cLinkInstagram}{cCorreo} {cDNI}{cNombreyApellido} {idAnimales} {tipoanimal} {tipoestado}")
    return redirect("/")
#f"El tipo de animal seleccionado tiene el ID:{cCasaDepartamento}{dFechaNacimiento}{cTelefono} {cNombreyApellido} {idAnimales} {tipoanimal} {tipoestado}"

