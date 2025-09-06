# Writing
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Appending
with open("file.txt", "a") as f:
    f.write("More text\n")

# Reading full content
with open("file.txt", "r") as f:
    print(f.read())

# Reading one line at a time
with open("file.txt", "r") as f:
    print(f.readline())

# Reading all lines into list
with open("file.txt", "r") as f:
    lines = f.readlines()

# Writing multiple lines from a list
lines = ["A\n", "B\n"]
with open("file.txt", "w") as f:
    f.writelines(lines)

# Check file exists
import os
os.path.exists("file.txt")

# Delete file
os.remove("file.txt")
