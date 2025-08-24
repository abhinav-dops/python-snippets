import json

data = {
    "name" : "Abhinav",
    "age" : 20,
    "Language" : "python"
}

with open ("data.json", "w") as file:
    json.dump(data,file)

print("data save to data.json")

with open ("data.json" ,"r" )as file:
    loaded = json.load(file)
    print("Loaded JSON as dictionary:")
    print(loaded)
h
#converting json string to python dictionary

import json

json_string = '{"name": "Abhinav", "age": 20, "language": "Python"}'
print("Type : ", type(json_string))
data = json.loads(json_string)
print("Type : ", type(data))
print("data: " , data)
print(data["name"])




