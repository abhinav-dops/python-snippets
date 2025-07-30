age = 18

#if else is used for conditional statements

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")
