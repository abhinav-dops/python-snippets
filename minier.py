try:
    number = int(input("Enter a number : "))
    result = 100/number
    print("Result: ", result)

except Exception as e:
    print("an error occured : " , e)