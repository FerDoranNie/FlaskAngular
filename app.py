import os
from flask import Flask
from flask_mysqldb import MySQL
app= Flask(__name__)
"""
esta linea será para la configuración de heroku

##app.config.from_object(os.environ['APP_SETTINGS'])

"""
@app.route("/")
def hello():
    return "Conociendo Flask"
@app.route("/<name>")
def hello_name(name):
    return "Hola {}!".format(name)

"""
Agregando la conexión a base de datos
"""
mysql = MySQL()
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='base10Data'
app.config['MYSQL_DATABASE_DB']= 'flaskBase'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)
con = mysql.connect()
cursor  = conn.cursor()
print (conn)


if __name__ == '__main__':
    app.run()


