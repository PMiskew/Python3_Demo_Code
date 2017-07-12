import math

num = input("Input number: ")

try:
    num = int(num)
    result = math.sqrt(num)
    print("The square root of "+str(num)+" is "+str(result))
except ValueError:
    print("You can't take the square root of "+num)

