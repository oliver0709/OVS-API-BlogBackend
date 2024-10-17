from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
import os
# Crear el blueprint para auth
auth_bp = Blueprint('auth_bp', __name__)

# Usuarios simulados-admin
users = {
    os.environ.get('USER_EMAIL'): os.environ.get('USER_PASSWORD')
}

# Ruta para login
@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    
    if users.get(email) != password:
        return jsonify({"msg": "Bad credentials"}), 401
    
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200

# Ruta protegida
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="This is a protected route")
