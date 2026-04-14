import json

users : dict

with open("file.json", "r") as archivo:
    json_data = json.load(archivo)
    users = json_data



users.update({"name": "Yoshino"})

with open("file.json", "w" , encoding="utf-8") as archivo:
    json.dump(users, archivo)