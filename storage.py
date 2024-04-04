import json
from datetime import datetime


def load_data():
    try:
        with open("customers.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"customers": [], "transactions": []}
    return data


def save_data(data):
    with open("customers.json", "w") as file:
        json.dump(data, file, indent=4)





