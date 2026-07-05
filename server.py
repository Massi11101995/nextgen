from flask import Flask, request, jsonify
from flask_cors import CORS  
import sqlite3

app = Flask(__name__)
CORS(app)  # Autoriser le front-end local
DB_FILE = 'reservations.db'

# Créer la table si elle n'existe pas
conn = sqlite3.connect(DB_FILE)
conn.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    panier TEXT,
    campus TEXT,
    code TEXT,
    date TEXT
)
''')
conn.close()

# Ajouter une réservation
@app.route('/api/reservations', methods=['POST'])
def add_reservation():
    data = request.json
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "INSERT INTO reservations (panier, campus, code, date) VALUES (?, ?, ?, ?)",
        (data['panier'], data['campus'], data['code'], data['date'])
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Réservation ajoutée', 'code': data['code']})

# Lister toutes les réservations (optionnel)
@app.route('/api/reservations', methods=['GET'])
def list_reservations():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

