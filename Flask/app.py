from flask import Flask
#Se crea una instancia de Flask, que es la aplicación web.
app = Flask(__name__)

if __name__ == '__main__':
    #port es el puerto donde se ejecutará la aplicación y debug=True activa el modo de depuración.
    app.run(port=3000, debug=True)
    