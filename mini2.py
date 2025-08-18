n = int(input("Enter number of profiles: "))

profiles = []

for i in range(n):

    profile = {}
   
    name = input("Enter your name: ")
    age = int(input("Enter your Age: "))
    favorite_language = input("Enter your favorite language: ")

    profile["name"] = name
    profile["age"] = age
    profile["favorite_language"] = favorite_language

    profiles.append(profile)

print("Your Profiles: ")
for i in range(len(profiles)):
    print("Profile", i+1, ":")

    for key, value in profile[i].items():
        print(f"{key} : {value}")


kj;l

