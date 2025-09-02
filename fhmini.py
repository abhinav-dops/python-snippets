with open("log.txt", "w") as file:
    file.write("Abhinav")
    file.write("\nPython")
    file.write("\n15")

#readline and readlines

#readline: One line at a time.
with open("log.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print("Line 1:", line1)
    print("Line 2:", line2)

#readlines: read all lines into a list.
with open("log.txt", "r") as file:
    lines = file.readlines()
    print(lines)

