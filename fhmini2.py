tasks = ["Wake up\n", "Study Python\n", "Practice DevOps\n"]

with open("tasks.txt", "w") as file:
    file.writelines(tasks)

with open("tasks.txt" , "r") as file:
    lines = file.readlines()
    print(lines)

with open("tasks.txt", "a") as file:
    file.write("Take a break\n")
    file.write("Go for a walk\n")

with open("tasks.txt" , "r") as file:
    lines = file.readlines()
    print(lines)

import os

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        print(file.read())

else:
    print("file not found!")

if os.path.exists("tasks.txt"):
    os.remove("tasks.txt")
    print("tasks.txt deleted")
file handle mini 
else:

    print("file does not exist.")

