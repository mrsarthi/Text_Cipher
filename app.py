from flask import Flask, render_template, request, jsonify
from enc_dec import encrypt, decrypt

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/encrypt", methods=["POST"])
def encrypt_text():
    data = request.json
    user_input = data.get("message", "")
    encrypted_text = encrypt(user_input)
    return jsonify({"encrypted": encrypted_text})


@app.route("/decrypt", methods=["POST"])
def decrypt_text():
    data = request.json
    encrypted_input = data.get("message", "")
    decrypted_text = decrypt(encrypted_input)
    return jsonify({"decrypted": decrypted_text})


if __name__ == '__main__':
    app.run(debug=True)
