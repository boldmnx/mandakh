import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "array": [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Alice", "age": 25, "city": "Los Angeles"},
        {"name": "Bob", "age": 35, "city": "Chicago"},
        {"name": "Emily", "age": 28, "city": "San Francisco"}
    ]
}


with open('data.json', 'w') as json_file:
    # python to json 
    json_string = json.dumps(data)
    json_file.write(json_string)

with open('data.json', 'r') as json_file:
    loaded_json_string = json_file.read()
    # json to python 
    loaded_data = json.loads(loaded_json_string)
    print("Loaded data:", loaded_data)
