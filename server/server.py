from  flask import Flask,request,jsonify,send_from_directory
import util
import os
app = Flask(__name__)

# This tells Flask to look for your UI in the ../client folder
app = Flask(__name__, static_url_path='', static_folder='../client')

util.load_saved_artifacts()

# This route serves your app.html when someone visits the main link
@app.route('/')
def index():
    return send_from_directory('../client', 'app.html')
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-origin', '*')

    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("Starting python flask for prediction success")
    app.run(host="0.0.0.0", port=port)