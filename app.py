from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# ✅ CONNECT TO MYSQL (from environment variables)
db = mysql.connector.connect(
    host=os.getenv("MYSQLHOST", "localhost"),
    user=os.getenv("MYSQLUSER", "root"),
    password=os.getenv("MYSQLPASSWORD", "Maria@bh25"),
    database=os.getenv("MYSQLDATABASE", "woodburyDB")
)

cursor = db.cursor()

# ✅ HOME ROUTE
@app.route('/')
def home():
    return "Woodbury Backend Running ✅"

# ✅ ADD RESERVATION
@app.route('/add_reservation', methods=['POST'])
def add_reservation():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        guests = data.get('guests')

        query = "INSERT INTO reservations (name, email, guests) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, guests))
        db.commit()

        return jsonify({"message": "Reservation added successfully!"})
    
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"message": "Error occurred"}), 500

# ✅ GET DATA
@app.route('/get_reservations', methods=['GET'])
def get_reservations():
    cursor.execute("SELECT * FROM reservations")
    data = cursor.fetchall()
    return jsonify(data)

# ✅ RUN APP
if __name__ == '__main__':
    app.run(debug=True)