make o
fruits = ["apple", "banana", "cherry"]

print(fruits[0])     # Output: apple
print(fruits[-1])    # Output: cherry (last item)

fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']


fruits.append("mango")     # Adds to the end
fruits.insert(1, "grape")  # Inserts at index 1
fruits.remove("cherry")    # Removes by value
fruits.pop()               # Removes last item
fruits.pop(0)              # Removes by index

print(len(fruits))         # Number of items

for fruit in fruits:
    print(fruit)

fruits.sort()              # Sorts alphabetically
fruits.sort(reverse=True)  # Sorts in reverse order
fruits.reverse()           # Reverses current order

colors = ["red", "blue", "green"]
colors.append("yellow")
colors.insert(1, "black")
colors.remove("blue")
colors.sort()
colors.reverse()

for color in colors:
    print(color)

