my_dict = {
    "name" : "Abhinav",
    "age" : 20,
    "language" : "python",
    'home' : 'india'
}

my_dict["city"] = 'delhi'
my_dict["age"] = 25

print(my_dict["age"])
print(my_dict)

print(my_dict.get("college", "Not found"))  # ✅ Safe

for key in my_dict:
    print(key)

for key, value in my_dict.items():
    print(key, ":", value)

for value in my_dict.items():
    print(value)
jlks

#Method	What it does
#dict.keys()	Returns all keys
#dict.values()	Returns all values
#dict.items()	Returns key-value pairs
#dict.get(k)	Safely gets a value by key
#dict.pop(k)	Removes a key
#k in dict	Checks if key exists


print(my_dict.get("name"))

