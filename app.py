from flask import Flask , request , jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
from marshmallow import Schema, fields, validate


app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

#drawing schema validate the datas that  willl be stored
class UserSchema(Schema):
    id = fields.Int(required=True)
    user = fields.Str(required=True, validate=validate.Length(min=2))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6)) 

user_schema = UserSchema()

def serialize_document(doc):
    "converting mongodb documents to serializable document to further jsonify it"
    if isinstance(doc, dict):
        return {key: serialize_document(value) for key, value in doc.items()}
    elif isinstance(doc, ObjectId):
        return str(doc)
    elif isinstance(doc, list):
        return [serialize_document(item) for item in doc]
    return doc

# 1. Add data through post Done 
@app.route("/add" , methods=['POST'])
def home():
    data = request.json
    if not data:
        return jsonify({'error': 'no data provided'}) , 400
    user_schema.load(data)
    result = mongo.db.mycollection.insert_one(data)
    
    return jsonify({'data insereted': 'successful'})

#2. Returns a list of all users Done
@app.route("/user" , methods=['GET'])
def get_all_user():
    documents = mongo.db.mycollection.find()
    data = [serialize_document(doc) for doc in documents]
    return jsonify(data) , 200    

#3. Returns a specific user Done
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
        user_id = int(id)
        user = mongo.db.mycollection.find_one({'id': user_id})
        if user is None:
            return jsonify({"user": "not found"}) , 404
        user = serialize_document(user)
        return jsonify(user), 200
    
#4. updates the user
@app.route("/update/user/<id>" , methods=['PUT'])
def update_user(id):
    user_id = int(id)
    user = mongo.db.mycollection.find_one({"id" : user_id})
    if user is None:
        return jsonify({"user": "not found"}) , 404
    new_data = request.json
    user_schema.load(new_data)
    
    mongo.db.mycollection.update_one({"id": user_id}, {"$set": new_data})
    
    updated_user = mongo.db.mycollection.find_one({"id": user_id})
    updated_user = serialize_document(updated_user)
    return jsonify(updated_user) , 200
    
    
#5. delete a specific user Done
@app.route('/delete/user/<id>' , methods=['DELETE'])
def delete_user(id):
    result = mongo.db.mycollection.delete_one({"id": id})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)