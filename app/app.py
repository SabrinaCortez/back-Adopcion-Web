from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from controller import *
import MySQLdb.cursors


app = Flask(__name__)
app.secret_key = 'your_secret_key' # Cambia esto por una clave secreta segura

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'adopciones'

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

# @app.route('/listadoadoptantes')
# def listadoadoptantes():
#     title="Listado Adoptantes"
#     print(f"session {session['loggedin']}")
#     if 'loggedin' in session :
#         logeado = session['loggedin']
#         if logeado:
#             adoptantes = adoptante_solicitudes()
#             return render_template("listadoAdoptantes.html",title=title,adoptantes= adoptantes)
#         return redirect(url_for('login'))    
#     return redirect(url_for('login'))

@app.route('/listadoadoptantes', methods=['GET', 'POST'])
def listadoadoptantes():
    title = "Listado Adoptantes"
    if 'loggedin' in session:
        logeado = session['loggedin']
        if logeado:
            if request.method == 'POST':
                cNombre = request.form['cNombre']
                cRaza = request.form['cRaza']
                cEdad = request.form['cEdad']
                cCondicionEspecial = request.form['cCondicionEspecial']
                cSexo = request.form['cSexo']
                cidTipoAnimal = request.form['cidTipoAnimal']
                cImagen = request.form['cImagen']
                
                cursor = mysql.connection.cursor()
                cursor.execute('INSERT INTO animales (cNombre, cRaza, cEdad, cCondicionEspecial, cSexo, cidTipoAnimal, cImagen) VALUES (%s, %s, %s, %s, %s, %s, %s)', 
                               (cNombre, cRaza, cEdad, cCondicionEspecial, cSexo, cidTipoAnimal, cImagen))
                mysql.connection.commit()
                cursor.close()
                flash('Animal agregado exitosamente!', 'success')

            adoptantes = adoptante_solicitudes()
            tipoAnimales = obtener_TipoAnimales()  # Función que obtenga los tipos de animales
            return render_template("listadoAdoptantes.html", title=title, adoptantes=adoptantes, tipoAnimales=tipoAnimales)
        return redirect(url_for('login'))
    return redirect(url_for('login'))

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

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuario WHERE usuario = %s', (usuario,))
        user = cursor.fetchone()
        cursor.close()
        print('validando ...')
        if user and bcrypt.check_password_hash(user['contrasena'], password):
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['usuario']
            flash('Has iniciado sesión exitosamente!', 'success')
            return redirect(url_for('listadoadoptantes'))
        
        else:
            session.pop('loggedin', None)
            session.pop('id', None)
            session.pop('username', None)
            flash('Nombre de usuario/contraseña incorrectos', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('login'))

# Ruta de registro
@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO usuario (usuario, contrasena) VALUES (%s, %s)', (usuario, hashed_password))
        mysql.connection.commit()
        cursor.close()
        flash('Te has registrado exitosamente!', 'success')
        return redirect(url_for('login'))
    return render_template('registrarse.html')
