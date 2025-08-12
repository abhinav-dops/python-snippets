colors = ("red", "green", "blue")

single = ("apple",)   # Tuple
not_a_tuple = ("apple")  # Just a string

print(colors[0])      # red
print(colors[-1])     # blue

for color in colors:
    print(color)

colors[1] = "yellow"   # Error: 'tuple' object does not support item assignment

nums = (1, 2, 2, 3, 4)
print(nums.count(2))     # Output: 2
print(nums.index(3))     # Output: 3
