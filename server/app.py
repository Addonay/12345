from flask import Flask, request, jsonify
from flask_cors import CORS
from models import User, db

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "db": "test",
    "host": "mongodb://localhost:27017/test"
}

db.init_app(app)
CORS(app, supports_credentials=True)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if the email is already registered
    existing_user = User.objects(email=data.get('email')).first()
    if existing_user:
        return jsonify({'message': 'Email is already registered'}), 400

    # Create a new user
    user = User(
        name=data.get('name'),
        email=data.get('email'),
        password=data.get('password')
    )
    user.save()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Find the user by email
    user = User.objects(email=data.get('email')).first()

    # Check if the user exists and the password is correct
    if user and user.password == data.get('password'):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid email or password'}), 401

if __name__ == "__main__":
    app.run(debug=True)
