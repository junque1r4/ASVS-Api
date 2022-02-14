from pymongo import MongoClient
import json

# TODO: Implement a variable for each collection on the DB.
connection = MongoClient("mongodb://localhost/auth_nist")
collection = connection.nist.data

def get_json_file():
    path = 'Config/NIST_File/nist_sanitized.json'
    with open(path) as file:
        all_data = json.load(file)

    return all_data