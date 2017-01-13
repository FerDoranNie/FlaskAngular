import os
from flask import Flask
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

if __name__ == '__main__':
    app.run()
