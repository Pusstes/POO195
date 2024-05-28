from flask import Flask,request
#Se crea una instancia de Flask, que es la aplicación web.
app = Flask(__name__)

#ruta simple
@app.route('/')
def principal():
    return 'Hola Mundo'
#en esta ruta se muestra un mensaje de bienvenida, se puede acceder a ella desde la URL http://localhost:3000/bienvenido

#ruta doble
@app.route('/usuario')
@app.route('/saludar')
def saludos():
    return 'Hola Mundo GERARDO'   
#en esta ruta se muestra un mensaje de bienvenida, se puede acceder a ella desde la URL http://localhost:3000/saludar

#rutas con parametros
@app.route('/hi/<nombre>')
def hi(nombre):
    return f'Hola, {nombre}!'
#en esta ruta se muestra un mensaje de bienvenida, se puede acceder a ella desde la URL http://localhost:3000/hi/gerardo
#para cambiar el valor del parametro podriamos usar: float:<nombre> o int:<nombre> o path:<nombre> o cualquier otro tipo de dato

#Definicion de metodos de trabajo
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'GET':
        return 'No es seguro mandar pass por GET'
    elif request.method == 'POST':
        return 'Datos enviados por POST, es seguro'

#menejo de excepciones para rutas no encontradas
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: PAGINA NO ENCONTRADA'
#en esta ruta se muestra un mensaje de error, se puede acceder a ella desde la URL http://localhost:3000/otra

if __name__ == '__main__':
    #port es el puerto donde se ejecutará la aplicación y debug=True activa el modo de depuración.
    app.run(port=3000, debug=True)
    