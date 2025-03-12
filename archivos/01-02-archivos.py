import json

data = {"name": "Alice", "age": 25, "city": "New York"}

with open("archivos/data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("archivos/data.json", "r") as file:
    data = json.load(file)
    print(type(data))
