from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
        return render_template('formulario.html')
    
@app.route('/numeroalcuadrado/<int:numero>')
def numero(numero):
    return f'El numero al cuadrado es {numero*numero}'

@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: PAGINA NO ENCONTRADA'

if __name__ == '__main__':
    app.run(port =3000,debug=True)