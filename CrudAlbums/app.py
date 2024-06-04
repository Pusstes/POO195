from flask import Flask,request,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost' #host de la base de datos
app.config['MYSQL_USER'] = 'root' #usuario de la base de datos
app.config['MYSQL_PASSWORD'] = '' #contraseña de la base de datos
app.config['MYSQL_DB'] = 'bdflask' #nombre de la base de datos

MySQL = MySQL(app) #se crea una instancia de MySQL

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardarAlbum', methods=['POST']) #ruta para guardar un album
def guardarAlbum(): #funcion para guardar un album
    if request.method == 'POST': #validacion del metodo
        titulo = request.form['titulo']
        artista = request.form['artista']
        anio = request.form['anio']
        #valores que se obtienen del formulario
        print(titulo, artista, anio)
        return 'Recibido'   

#menejo de excepciones para rutas no encontradas
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: PAGINA NO ENCONTRADA'
#en esta ruta se muestra un mensaje de error, se puede acceder a ella desde la URL http://localhost:3000/otra

if __name__ == '__main__':
    #port es el puerto donde se ejecutará la aplicación y debug=True activa el modo de depuración.
    app.run(port=4000, debug=True)