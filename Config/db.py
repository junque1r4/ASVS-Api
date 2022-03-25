from pymongo import MongoClient
from credentials import LOCAL
import json

# TODO: Implement a variable for each collection on the DB.
connection = MongoClient(f"mongodb+srv://{LOCAL}")
collection = connection.auth_nist.data


def get_json_file():
    path = "Config/NIST_File/nist_sanitized.json"
    with open(path) as file:
        all_data = json.load(file)

    return all_data
