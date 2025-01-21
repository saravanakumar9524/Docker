from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend to communicate with the backend

# Feedback endpoint
@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    feedback = data.get('feedback')
    if feedback:
        print(f"Received feedback: {feedback}")
        return jsonify({"message": "Feedback received. Thank you!"}), 200
    else:
        return jsonify({"message": "Feedback cannot be empty."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
