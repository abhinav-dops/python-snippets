import json

# --------------------------------------
# 1️⃣ json.load() - Read JSON from a file
# --------------------------------------
print(" Reading JSON from file (load):")
with open("data.json", "r") as f:
    file_data = json.load(f)
print(file_data)
print()

# --------------------------------------
# 2️⃣ json.loads() - Read JSON from a string
#convert json string -> python object
# --------------------------------------
print(" Reading JSON from string (loads):")
json_str = '{"name": "Abhinav", "skills": ["Python", "Git"]}'
parsed_data = json.loads(json_str)
print(parsed_data)
print()

# --------------------------------------
# 3️⃣ json.dump() - Write JSON to a file
#json.dump() Purpose: Write (or "dump") Python data into a JSON file
# --------------------------------------
print(" Writing JSON to file (dump):")
to_write = {"project": "DevOps", "duration": "6 months"}
with open("output.json", "w") as f:
    json.dump(to_write, f, indent=2)
print("✔ Data written to output.json")
print()

# --------------------------------------
# 4️⃣ json.dumps() - Convert Python object to JSON string
# --------------------------------------
print(" Converting Python object to JSON string (dumps):")
json_text = json.dumps(to_write, indent=2)
print(json_text)



