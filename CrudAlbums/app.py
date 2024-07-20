from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL
import os # Para guardar archivos
from werkzeug.utils import secure_filename # Para guardar archivos
from flask import send_from_directory # Para mostrar archivos

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'
mysql = MySQL(app)
app.secret_key = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = 'C:/Users/ulqui/Desktop/UPQ/6to_cuatri/POO/POO195/CrudAlbums/static/UPLOADS' # Ruta donde se guardarán las imágenes
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg'} # Extensiones permitidas

# Función para verificar si el archivo tiene una extensión permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Ruta para mostrar la imagen
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def index():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM albums')
        consultaA = cursor.fetchall()
        return render_template('index.html', albums=consultaA)
    except Exception as e:
        print(e)
        return render_template('error.html', error_message=str(e))
    
@app.route('/guardarAlbum', methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        Ftitulo = request.form['titulo']
        Fartista = request.form['artista']
        Fanio = request.form['anio']
        file = request.files['portada']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # Guardar archivo en la ruta especificada
            
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO albums(titulo, artista, anio, portada) VALUES(%s, %s, %s, %s)', (Ftitulo, Fartista, Fanio, filename))
            mysql.connection.commit()
            flash('Álbum guardado correctamente', 'success')
        else: # Si no se selecciona un archivo
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO albums(titulo, artista, anio, portada) VALUES(%s, %s, %s, %s)', (Ftitulo, Fartista, Fanio, None))
            mysql.connection.commit()
            flash('Álbum guardado sin portada', 'success') 
        
        return redirect(url_for('index'))
    
@app.route('/editar/<id>')
def editar(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM albums WHERE idAlbum=%s', [id])
    albumE = cur.fetchone()
    return render_template('editar.html', album=albumE)

@app.route('/ActualizarAlbum/<id>', methods=['POST'])
def ActualizarAlbum(id):
    if request.method == 'POST':
        try:
            Ftitulo = request.form['txtTitulo']
            Fartista = request.form['txtArtista']
            Fanio = request.form['txtAnio']
            file = request.files['portada']
            
            cursor = mysql.connection.cursor()

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cursor.execute('UPDATE albums SET titulo=%s, artista=%s, anio=%s, portada=%s WHERE idAlbum=%s', (Ftitulo, Fartista, Fanio, filename, id))
            else:
                cursor.execute('UPDATE albums SET titulo=%s, artista=%s, anio=%s WHERE idAlbum=%s', (Ftitulo, Fartista, Fanio, id))
            
            mysql.connection.commit()
            flash('Álbum editado correctamente', 'info')
        
        except Exception as e:
            flash('Error al guardar el álbum: ' + str(e))
        
        return redirect(url_for('index'))

@app.route('/eliminar/<id>')
def eliminarAlbum(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM albums WHERE idAlbum=%s', [id])
        mysql.connection.commit()
        flash('Álbum eliminado correctamente', 'danger')
        return redirect(url_for('index'))
    except Exception as e:
        flash('Error al eliminar el álbum: ' + str(e))
        return redirect(url_for('index'))

@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontré nada'

if __name__ == '__main__':
    app.run(port=4000, debug=True)

