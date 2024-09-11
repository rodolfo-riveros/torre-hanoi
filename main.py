import os
import sys
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Agregar la carpeta 'src' al sys.path para poder importar el módulo correctamente
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from torres_de_hanoi import TorresDeHanoi  # Importamos la clase TorresDeHanoi desde src/torres_de_hanoi.py

app = Flask(__name__, template_folder='src/templates')

# Inicialización de la instancia del juego
hanoi = None

@app.route('/')
def index():
    global hanoi
    # Inicializar el juego si aún no está configurado
    if hanoi is None:
        hanoi = TorresDeHanoi(3)  # Número predeterminado de discos

    estado = hanoi.estado()  # Obtenemos el estado actual de las torres
    error = request.args.get('error', 'false')  # Obtenemos si hubo un error
    num_discos = hanoi.num_discos  # Obtener el número de discos actual
    return render_template('index.html', estado=estado, error=error, num_discos=num_discos)

@app.route('/iniciar', methods=['POST'])
def iniciar_juego():
    global hanoi
    num_discos = int(request.form['num_discos'])  # Obtener el número de discos del formulario
    hanoi = TorresDeHanoi(num_discos)  # Crear una nueva instancia del juego con el número seleccionado
    return redirect(url_for('index'))  # Redirigir a la página principal para mostrar el juego

@app.route('/estado')
def obtener_estado():
    return jsonify(hanoi.estado())  # Retorna el estado de las torres en formato JSON

@app.route('/mover', methods=['POST'])
def mover():
    global hanoi
    origen = request.form['origen']
    destino = request.form['destino']
    if hanoi.mover(origen, destino):
        return redirect(url_for('index'))  # Si el movimiento es válido, redirige a la página principal
    else:
        return redirect(url_for('index', error='true'))  # Si es inválido, redirige con error

# Iniciar la aplicación Flask en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)