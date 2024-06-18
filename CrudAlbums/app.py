from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'
mysql = MySQL(app)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM albums')
        consultaA = cursor.fetchall()
        return render_template('index.html', albums=consultaA)
    except Exception as e:
        print(e)
        # Retorna una respuesta en caso de error
        return render_template('error.html', error_message=str(e))

@app.route('/guardarAlbum', methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        Ftitulo = request.form['titulo']
        Fartista = request.form['artista']
        Fanio = request.form['anio']

        # Enviamos a la BD
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO albums(titulo, artista, anio) VALUES(%s, %s, %s)', (Ftitulo, Fartista, Fanio))
        mysql.connection.commit()
        flash('Album Guardado Correctamente')
        return redirect(url_for('index'))

# Manejo de excepciones
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontré nada'

if __name__ == '__main__':
    # port es el puerto donde se ejecutará la aplicación y debug=True activa el modo de depuración.
    app.run(port=3000, debug=True)
