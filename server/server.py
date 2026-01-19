from flask import Flask, request, jsonify, send_from_directory
import util
import os

# This finds exactly where your server.py is sitting
current_dir = os.path.dirname(os.path.abspath(__file__))
# This points to the client folder relative to this file
client_dir = os.path.join(current_dir, '..', 'client')

app = Flask(__name__, static_url_path='', static_folder=client_dir)

util.load_saved_artifacts()

@app.route('/')
def index():
    return send_from_directory(client_dir, 'app.html')

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({'locations': util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)