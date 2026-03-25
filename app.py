from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# In-memory storage for reservations (temporary)
reservations = []

# Serve frontend
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_files(path):
    return send_from_directory('.', path)

# Add reservation (no DB)
@app.route('/add_reservation', methods=['POST'])
def add_reservation():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        guests = data.get('guests')

        # Save in memory
        reservations.append({
            "name": name,
            "email": email,
            "guests": guests
        })

        print("📩 New Reservation:", name, email, guests)
        return jsonify({"message": "Reservation added successfully!"})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"message": "Something went wrong"}), 500

# Get reservations (in-memory)
@app.route('/get_reservations', methods=['GET'])
def get_reservations():
    return jsonify(reservations)

# Run app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    