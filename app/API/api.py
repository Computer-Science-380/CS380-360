import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("API script is running...")
from flask import Flask, request, jsonify
from flask_cors import CORS
from ciphers.morse import Morse

##from ciphers.bacon import encrypt as bacon_encrypt
##from ciphers.caesar import encryot as caesar_encrypt


app = Flask(__name__)
CORS(app)


@app.route("/api/morse", methods=["POST"])
def encrypt_morse():
    if not request.is_json:
        return jsonify({"error": "Invalid content type"}), 400

    data = request.get_json()

    if "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 400

    message = data["message"]

    cipher = Morse(message)

    encoded_message = cipher.encrypt()

    return jsonify({"result": encoded_message}), 200


if __name__ == "__main__":
    app.run(debug=True)
