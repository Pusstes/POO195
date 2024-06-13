from flask import Flask,request,render_template,url_for,redirect,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost' #host de la base de datos
app.config['MYSQL_USER'] = 'root' #usuario de la base de datos
app.config['MYSQL_PASSWORD'] = '' #contraseña de la base de datos
app.config['MYSQL_DB'] = 'bdflask' #nombre de la base de datos

app.secret_key = 'my_secret'

MySQL = MySQL(app) #se crea una instancia de MySQL

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/GuardarMedico', methods=['POST'])
def guardarMedico():
    if request.method == 'POST':
        frfc = request.form['rfc']
        fnombre = request.form['nombre']
        fcedula = request.form['cedula']
        fcorreo = request.form['correo']
        fpass = request.form['pass']
        frol = request.form['rol']
        cursor = MySQL.connection.cursor()
        cursor.execute('INSERT INTO t_medicos (rfc, nombre, cedula, correo, pass, rol) VALUES (%s, %s, %s, %s, %s, %s)', (frfc, fnombre, fcedula, fcorreo, fpass, frol))
        flash('El medico fue registrado Correctamente')
        return redirect(url_for('registro'))

#menejo de excepciones para rutas no encontradas
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: PAGINA NO ENCONTRADA'
#en esta ruta se muestra un mensaje de error, se puede acceder a ella desde la URL http://localhost:3000/otra

if __name__ == '__main__':
    #port es el puerto donde se ejecutará la aplicación y debug=True activa el modo de depuración.
    app.run(port=4000, debug=True)
    