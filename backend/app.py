from flask_cors import CORS
from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Configuración desde variables de entorno o valores por defecto
DB_HOST = os.environ.get("DB_HOST", "db")           # nombre del servicio en docker-compose
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "123456")
DB_NAME = os.environ.get("DB_NAME", "app_db")

#Función para conectar con la base de datos
def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route('/')
def home():
    return jsonify({"mensaje": "API Flask + MySQL funcionando"})

@app.route('/usuarios')
def obtener_usuarios():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM usuarios")
        usuarios = [{"id": row[0], "nombre": row[1]} for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return jsonify(usuarios)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/usuarios', methods=['POST'])
def insertar_usuario():
    try:
        datos = request.get_json()
        nombre = datos.get("nombre")

        if not nombre:
            return jsonify({"error": "Falta el campo 'nombre'"}), 400

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s)", (nombre,))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"mensaje": f"Usuario '{nombre}' agregado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/boletos', methods=['POST'])
def comprar_boleto():
    try:
        datos = request.get_json()
        usuario_id = datos.get("usuario_id")
        evento = datos.get("evento")
        cantidad = datos.get("cantidad")

        if not usuario_id or not evento or not cantidad:
            return jsonify({"error": "Datos incompletos"}), 400

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO boletos (usuario_id, evento, cantidad) VALUES (%s, %s, %s)",
                       (usuario_id, evento, cantidad))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"mensaje": f"Boleto para '{evento}' comprado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/conciertos', methods=['GET'])
def obtener_conciertos():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, precio FROM conciertos")
        conciertos = [{"id": row[0], "nombre": row[1], "precio": float(row[2])} for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return jsonify(conciertos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/conciertos', methods=['POST'])
def agregar_concierto():
    try:
        datos = request.get_json()
        nombre = datos.get("nombre")
        precio = datos.get("precio")

        if not nombre or precio is None:
            return jsonify({"error": "Faltan datos"}), 400

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO conciertos (nombre, precio) VALUES (%s, %s)", (nombre, precio))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"mensaje": f"Concierto '{nombre}' agregado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
