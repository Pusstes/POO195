from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'  # host de la base de datos
app.config['MYSQL_USER'] = 'root'  # usuario de la base de datos
app.config['MYSQL_PASSWORD'] = ''  # contraseña de la base de datos
app.config['MYSQL_DB'] = 'hospital'  # nombre de la base de datos

app.secret_key = 'my_secret'

mysql = MySQL(app)  # se crea una instancia de MySQL

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/consulta')
def consulta():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM medicos')
    medicos = cursor.fetchall()
    cursor.close()
    return render_template('Consulta.html', medicos=medicos)

@app.route('/GuardarMedico', methods=['POST'])
def guardarMedico():
    if request.method == 'POST':
        frfc = request.form['rfc']
        fnombre = request.form['nombre']
        fcedula = request.form['cedula']
        fcorreo = request.form['correo']
        fpass = request.form['pass']
        frol = request.form['rol']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO medicos (rfc, nombre, cedula, correo, pass, rol) VALUES (%s, %s, %s, %s, %s, %s)', (frfc, fnombre, fcedula, fcorreo, fpass, frol))
        mysql.connection.commit()
        cursor.close()
        flash('El médico fue registrado correctamente')
        return redirect(url_for('consulta'))

#ruta para editar un registro
@app.route('/editar/<string:id>')
def editar(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM medicos WHERE id = {0}'.format(id))
    medicoE = cursor.fetchone()
    cursor.close()
    return render_template('editar.html', medico=medicoE)

#ruta para actualizar un registro
@app.route('/ActualizarMedico/<string:id>', methods=['POST'])
def actualizarMedico(id):
    if request.method == 'POST':
        try:
            frfc = request.form['rfc']
            fnombre = request.form['nombre']
            fcedula = request.form['cedula']
            fcorreo = request.form['correo']
            fpass = request.form['pass']
            frol = request.form['rol']
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE medicos SET rfc=%s, nombre=%s, cedula=%s, correo=%s, pass=%s, rol=%s WHERE id = {0}'.format(id), (frfc, fnombre, fcedula, fcorreo, fpass, frol))
            mysql.connection.commit()
            cursor.close()
            flash('Registro actualizado correctamente')
            return redirect(url_for('consulta'))
        except Exception as e:
            flash('Error al actualizar el registro' + str(e))
            return redirect(url_for('consulta'))
    
#Ruta para eliminar un registro
@app.route('/eliminar/<string:id>')
def eliminar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM medicos WHERE id = {0}'.format(id))
        mysql.connection.commit()
        cursor.close()
        flash('Registro eliminado correctamente')
        return redirect(url_for('consulta'))
    except Exception as e:
        flash('Error al eliminar el registro' + str(e))
        return redirect(url_for('consulta'))

# Manejo de excepciones para rutas no encontradas
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: PAGINA NO ENCONTRADA'

if __name__ == '__main__':
    # puerto donde se ejecutará la aplicación y debug=True activa el modo de depuración.
    app.run(port=4000, debug=True)
