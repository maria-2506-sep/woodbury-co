from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Serve frontend
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_files(path):
    return send_from_directory('.', path)

# Form API
@app.route('/add_reservation', methods=['POST'])
def add_reservation():
    try:
        data = request.get_json()

        name = data.get('name')
        email = data.get('email')
        guests = data.get('guests')

        print("Reservation:", name, email, guests)

        return jsonify({"message": "Reservation added successfully!"})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"message": "Something went wrong"}), 500

# Run
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
      
