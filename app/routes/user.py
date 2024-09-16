from flask import Blueprint, request, jsonify
from app.models.schema import UserSchema
from services.fetch_users import get_users, add_user, update_user, delete_user, get_user_by_id

user = Blueprint('user', __name__)

user_schema = UserSchema()

@user.route("/", methods=['GET'])
def list_users():
    return jsonify(get_users()), 200

@user.route("/<id>", methods=['GET'])
def get_user(id):
    return get_user_by_id(id)

@user.route("/add", methods=['POST'])
def create_user():
    data = request.json
    return add_user(data)

@user.route("/update/<id>", methods=['PUT'])
def modify_user(id):
    data = request.json
    return update_user(id, data)

@user.route("/delete/<id>", methods=['DELETE'])
def remove_user(id):
    return delete_user(id)
