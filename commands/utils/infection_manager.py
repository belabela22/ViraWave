import json
import os

data_path = "data/outbreak.json"

def load_data():
    if not os.path.exists(data_path):
        return {"infected": {}, "vaccinated": [], "isolated": [], "mutation_level": 1}
    with open(data_path, "r") as file:
        return json.load(file)

def save_data(data):
    with open(data_path, "w") as file:
        json.dump(data, file, indent=4)

def check_infection_status(user_id):
    data = load_data()
    return data.get("infected", {}).get(str(user_id), None)

def mark_isolated(user_id):
    data = load_data()
    if str(user_id) not in data["isolated"]:
        data["isolated"].append(str(user_id))
    save_data(data)

def cure_user(user_id):
    data = load_data()
    data["infected"].pop(str(user_id), None)
    if str(user_id) not in data["vaccinated"]:
        data["vaccinated"].append(str(user_id))
    save_data(data)

def get_stats():
    data = load_data()
    return {
        "infected": len(data["infected"]),
        "vaccinated": len(data["vaccinated"]),
        "isolated": len(data["isolated"]),
        "mutation_level": data.get("mutation_level", 1)
    }
