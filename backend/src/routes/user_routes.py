from flask import Blueprint, jsonify, request
from services.user_service import UserService

user_bp = Blueprint('user', __name__)
user_service = UserService()

@user_bp.route('/user', methods=['GET'])
def get_all():
    return jsonify(user_service.get_all_users()), 200

@user_bp.route('/user/<uuid:user_id>', methods=['GET']) # Mudança aqui!
def get_one(user_id):
    user = user_service.get_user_by_id(str(user_id))
    return jsonify(user) if user else (jsonify({"error": "Not found"}), 404)

@user_bp.route('/user', methods=['POST'])
def create():
    user_service.create_user(request.json)
    return jsonify({"message": "Created"}), 201

@user_bp.route('/user/<uuid:user_id>', methods=['PUT']) # Mudança aqui!
def update(user_id):
    user_service.update_user(str(user_id), request.json)
    return jsonify({"message": "Updated"}), 200

@user_bp.route('/user/<uuid:user_id>', methods=['DELETE']) # Mudança aqui!
def delete(user_id):
    user_service.delete_user(str(user_id))
    return jsonify({"message": "Deleted"}), 200