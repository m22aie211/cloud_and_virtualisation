from flask import Flask, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient("mongodb://34.139.20.79:27017/")
db = client["assignment1"]
collection = db["mycollection"]


# Health Check Endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200


# Insertion Endpoint
@app.route('/insert', methods=['POST'])
def insert_data():
    try:
        data = request.get_json()
        if data:
            inserted_id = collection.insert_one(data).inserted_id
            return jsonify({"message": "Data inserted successfully", "id": str(inserted_id)}), 201
        else:
            return jsonify({"error": "No data provided"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# get data from DB
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        data_cursor = collection.find({})
        data_list = [doc for doc in data_cursor]

        if data_list:
            json_data = json.dumps(data_list, default=str)
            return json_data, 200
        else:
            return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
