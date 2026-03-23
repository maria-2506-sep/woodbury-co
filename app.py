from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Woodbury Backend Running ✅"


# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Maria@bh25",
    database="woodburyDB"
)

cursor = db.cursor()

# -------------------- CREATE --------------------
@app.route('/add_reservation', methods=['POST'])
def add_reservation():
    data = request.json
    name = data['name']
    email = data['email']
    guests = data['guests']

    query = "INSERT INTO reservations (name, email, guests) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, guests))
    db.commit()

    return jsonify({"message": "Reservation added successfully"})


# -------------------- READ --------------------
@app.route('/get_reservations', methods=['GET'])
def get_reservations():
    cursor.execute("SELECT * FROM reservations")
    results = cursor.fetchall()

    data = []
    for row in results:
        data.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "guests": row[3]
        })

    return jsonify(data)


# -------------------- UPDATE --------------------
@app.route('/update_reservation/<int:id>', methods=['PUT'])
def update_reservation(id):
    data = request.json
    name = data['name']
    email = data['email']
    guests = data['guests']

    query = "UPDATE reservations SET name=%s, email=%s, guests=%s WHERE id=%s"
    cursor.execute(query, (name, email, guests, id))
    db.commit()

    return jsonify({"message": "Reservation updated"})


# -------------------- DELETE --------------------
@app.route('/delete_reservation/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    query = "DELETE FROM reservations WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()

    return jsonify({"message": "Reservation deleted"})


# Run server
if __name__ == '__main__':
    app.run(debug=True)