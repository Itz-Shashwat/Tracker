from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To allow cross-origin requests

# Storage for live location (could be replaced by a database)
current_location = {}

@app.route('/api/updateLocation', methods=['POST'])
def update_location():
    global current_location
    data = request.get_json()
    if 'latitude' in data and 'longitude' in data:
        current_location = {
            "latitude": data['latitude'],
            "longitude": data['longitude'],
            "timestamp": data['timestamp']
        }
        return jsonify({"status": "success", "message": "Location updated!"}), 200
    return jsonify({"status": "error", "message": "Invalid data!"}), 400

@app.route('/api/getLocation', methods=['GET'])
def get_location():
    if current_location:
        return jsonify(current_location), 200
    return jsonify({"status": "error", "message": "No location available!"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
