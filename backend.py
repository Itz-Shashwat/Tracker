from flask import Flask, request, jsonify

app = Flask(__name__)

# Variable to store the last received location
latest_location = {"latitude": None, "longitude": None}


@app.route("/location", methods=["POST"])
def update_location():
    """Endpoint to receive location from the mobile app"""
    global latest_location
    data = request.json
    latest_location = data
    return jsonify({"message": "Location updated successfully"}), 200


@app.route("/get_location", methods=["GET"])
def get_location():
    """Endpoint to serve location to the Python program"""
    if latest_location["latitude"] is not None:
        return jsonify(latest_location), 200
    else:
        return jsonify({"error": "No location available yet"}), 404


if __name__ == "__main__":
    app.run(debug=True)
