from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated flag to request location from the app
send_location_flag = False


@app.route('/location-check', methods=['GET'])
def location_check():
    global send_location_flag
    if send_location_flag:
        send_location_flag = False  # Reset after reading
        return jsonify(True)
    return jsonify(False)


@app.route('/request-location', methods=['POST'])
def request_location():
    global send_location_flag
    send_location_flag = True
    return jsonify({"message": "Location request sent to the app"})


@app.route('/send-location', methods=['POST'])
def receive_location():
    data = request.json
    if not data or 'latitude' not in data or 'longitude' not in data:
        return jsonify({"error": "Invalid data"}), 400

    latitude = data['latitude']
    longitude = data['longitude']
    print(f"Received location: Latitude = {latitude}, Longitude = {longitude}")
    return jsonify({"message": "Location received successfully!"})


if __name__ == "__main__":
    app.run(debug=True)
