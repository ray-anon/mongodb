from flask import jsonify
from app.db import mongo  #to avoid circular import
from utils.serialize import serialize_document
from app.models.schema import UserSchema

user_schema = UserSchema()

def get_users():
    documents = mongo.db.mycollection.find()
    return [serialize_document(doc) for doc in documents]

def get_user_by_id(id):
    user = mongo.db.mycollection.find_one({'id': int(id)})
    if user is None:
        return jsonify({"user": "not found"}), 404
    return jsonify(serialize_document(user)), 200

def add_user(data):
    user_schema.load(data)
    result = mongo.db.mycollection.insert_one(data)
    return jsonify({'message': 'User added successfully'}), 201

def update_user(id, new_data):
    user_schema.load(new_data)
    result = mongo.db.mycollection.update_one({"id": int(id)}, {"$set": new_data})
    if result.matched_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({'message': 'User updated successfully'}), 200

def delete_user(id):
    result = mongo.db.mycollection.delete_one({"id": int(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200
