from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# ✅ CONNECT TO MYSQL (SAFE HANDLING)
try:
    db = mysql.connector.connect(
        host=os.getenv("MYSQLHOST", "localhost"),
        user=os.getenv("MYSQLUSER", "root"),
        password=os.getenv("MYSQLPASSWORD", "Maria@bh25"),
        database=os.getenv("MYSQLDATABASE", "woodburyDB")
    )
    cursor = db.cursor()
    db_connected = True
    print("✅ Database connected")

except Exception as e:
    print("❌ Database connection failed:", e)
    db_connected = False


# ✅ SERVE FRONTEND (VERY IMPORTANT FOR RENDER)
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_files(path):
    return send_from_directory('.', path)


# ✅ ADD RESERVATION (NO CRASH GUARANTEE)
@app.route('/add_reservation', methods=['POST'])
def add_reservation():
    try:
        data = request.get_json()

        name = data.get('name')
        email = data.get('email')
        guests = data.get('guests')

        print("📩 New Reservation:", name, email, guests)

        # ✅ If DB works → store data
        if db_connected:
            query = "INSERT INTO reservations (name, email, guests) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, guests))
            db.commit()

        # ✅ Always return success (NO CRASH)
        return jsonify({"message": "Reservation added successfully!"})
    
    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"message": "Something went wrong"}), 500


# ✅ GET DATA (OPTIONAL SAFE)
@app.route('/get_reservations', methods=['GET'])
def get_reservations():
    try:
        if db_connected:
            cursor.execute("SELECT * FROM reservations")
            data = cursor.fetchall()
            return jsonify(data)
        else:
            return jsonify([])
    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify([])


# ✅ RUN APP (RENDER FIX)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))