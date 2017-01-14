import os
from flask import Flask, request
from flask_mysqldb import MySQL
app= Flask(__name__)
"""
esta linea será para la configuración de heroku

##app.config.from_object(os.environ['APP_SETTINGS'])

"""

"""
Agregando la conexión a base de datos
"""
mysql = MySQL()
app.config['MYSQL_DATABASE_USER']='datascience'
app.config['MYSQL_DATABASE_PASSWORD']='base10Data'
app.config['MYSQ_DATABASE_DB']= 'prueba'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)



@app.route("/")
def hello():
    return "Conociendo Flask"

@app.route("/nombre/<name>")
def hello_name(name):
    return "Hola {}!".format(name)

@app.route("/Authenticate")
def Authenticate():
    username = request.args.get("UserName")
    password = request.args.get("Password")
    cursor = mysql.connect().cursor()
    print (cursor)
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
        return "Usuario y contraseña incorrectos"
    else:
        return "Buen logeo"




if __name__ == '__main__':
    app.run()


