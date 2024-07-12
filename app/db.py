# pip install pymysql
# pip freeze > requirements.txt
# pip install -r requirements.txt
# conectar bbdd -> host, user, pass, db

import pymysql
from pymysql import Error

# local -> wamp
host = "localhost"
user = "root"
clave= ""
db="adopciones"

# remota -> pythonenaywhere
# host = "adrianreciomdq.mysql.pythonanywhere-services.com"
# user = "adrianreciomdq"
# clave= "www.pythonanywhere.com"
# db="adrianreciomdq$adopciones"

def  conexionMySQL():
    try:
        # Establecer la conexión
        # print ("Tratando de conectarme ")
        conexion = pymysql.connect(host=host,user=user,password=clave,database=db)
        # Comprobar si la conexión fue exitosa
        if conexion:
            # print("Conexión exitosa a la base de datos")
            # pruebaListarAnimales(conexion)
            return conexion
    except Error as e:
        print("Error durante la conexión:", e)

def desConexionMySQL(connection):
    if connection:
        connection.close()
        print("Conexión cerrada")

def pruebaListarAnimales(conexion):
  # Ejemplo de consulta
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM animales;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)