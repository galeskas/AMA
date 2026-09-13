from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('amadata.db')
    conn.row_factory = sqlite3.Row
    return conn
# Nova rota para carregar a página web
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mamadas', methods=['POST'])
def create_mamada():
    data = request.json

    # Pega os dados do JSON enviado
    data_hora = data.get('data_hora')
    tipo_id = data.get('tipoID')
    status_id = data.get('statusID')
    quantidade = data.get('quantidade') # Pode ser None se for Natural

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Mamadas (Data_Hora, tipoID, statusID, Quantidade)
    VALUES (?, ?, ?, ?)
    ''', (data_hora, tipo_id, status_id, quantidade))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Mamada registrada com sucesso!'}), 201

@app.route('/mamadas', methods=['GET'])
def get_mamadas():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Mamadas')
    mamadas = cursor.fetchall()

    conn.close()

    return jsonify([dict(row) for row in mamadas])

@app.route('/mamadas/<int:mamada_id>', methods=['PUT'])
def update_mamada(mamada_id):
    data_hora = request.json.get('data_hora', None)
    tipo = request.json.get('tipo', None)
    quantidade = request.json.get('quantidade', None)

    conn = get_db_connection()
    cursor = conn.cursor()

    if data_hora:
        cursor.execute('UPDATE Mamadas SET Data_Hora = ? WHERE MamadaID = ?', (data_hora, mamada_id))
    if tipo:
        cursor.execute('UPDATE Mamadas SET Tipo = ? WHERE MamadaID = ?', (tipo, mamada_id))
    if quantidade:
        cursor.execute('UPDATE Mamadas SET Quantidade = ? WHERE MamadaID = ?', (quantidade, mamada_id))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Mamada atualizada com sucesso'})

@app.route('/mamadas/<int:mamada_id>', methods=['DELETE'])
def delete_mamada(mamada_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Mamadas WHERE MamadaID = ?', (mamada_id,))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Mamada deletada com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
