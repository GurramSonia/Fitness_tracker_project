from pymongo import MongoClient

def get_mongo_collection(collection_name):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["healthtracker"]
    return db["users"]