import json
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/detect', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    my_data = {}
    response = jsonify(my_data)
    response.status_code = 200

    return json.dumps(my_data)
