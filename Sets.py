set=  {1, 2, 3, 4, 5}

a = {1, 2, 3}
b = {2, 3, 4}
s = {}

print(a.union(b))       # {1, 2, 3, 4}
print(a.intersection(b))# {2, 3}
print(a.difference(b))  # {1}

a.add(5)
a.remove(2)

print(a|b)
print(a&b)
print(a-b)
print(a^b)

s.update(["yellow", "red"]) # Adds multiple items (duplicates ignored)
s.remove("green")   # Removes item; ❌ error if not found
s.discard("black")  # Removes item; ✅ no error if not found
s.pop()             # Removes a random item
s.clear()           # Empties the set



