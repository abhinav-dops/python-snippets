profile = {}
 fdlkjglkdsjfgdlkfj
name = input("Enter your name: ")
age = int(input("Enter your Age: "))
favorite_language = input("Enter your favorite language: ")

profile["name"] = name
profile["age"] = age
profile["favorite_language"] = favorite_language

print("Your Profile: ")
for key ,value in profile.items():
    print(key, ":" , value)



#nextminiproject 

student = {
    "name": "Abhinav",
    "age": 20,
    "course": "Python"
}

print(student)
print(student["name"])

student["age"] = 21
student["college"] = "Xyz"

for key, value in student.items():

    print(key, ":" , value)


