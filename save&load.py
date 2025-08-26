import json

expenses =  [
    {"amount": 100, "category": "Food", "note": "Lunch"},
    {"amount": 200, "category": "Travel", "note": "Taxi"}
]

with open("expenses.json" , "w") as file:
    json.dump(expenses,file)

with open("expenses.json", "r") as file:
    loaded_file = json.load(file)
    print(loaded_file)

print("Expeses loaded from Json: ")
for e in loaded_file:
    print(e)

for expense in loaded_file:
    print("Amount:", expense["amount"])
    print("Category:", expense["category"])

