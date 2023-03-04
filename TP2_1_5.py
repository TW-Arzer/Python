import math

def carré():
    str_number = input("Enter a number:\n")
    try:
        int_number = int(str_number)
        result = math.sqrt(int_number)
    except ValueError as e:
        print("Please try again with another number")
        carré()
    else:
        print(result)

carré()