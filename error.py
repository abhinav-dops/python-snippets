try:
    num = int(input("Enter a number: "))
    result = 10/num
    print("Result: " , result)

except ZeroDivisionError :
    print("you can't divide by zero!")
except ValueError :
    print("please enter a valid number!")
finally:

    print("Done.")

sd hahaha
