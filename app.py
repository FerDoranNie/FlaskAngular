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
app.config['MYSQL-DATABASE-PASSWORD']='base10Data'
app.config['MYSQL_DATABASE_DB']= 'flaskBase'
mysql.init_app(app)


if __name__ == '__main__':
    app.run()
