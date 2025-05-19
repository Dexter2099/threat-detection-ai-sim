from flask import Flask, request, jsonify
from model.predict import predict_threat
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so React can hit API

@app.route('/api/predict', methods=['POST'])
def detect():
    try:
        input_data = request.get_json()
        result = predict_threat(input_data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
