# Enter three numbers
number1 = float(input("Enter number1: "))
number2 = float(input("Enter number2: "))
number3 = float(input("Enter number3: "))

if number1 > number2:
    number1, number2 = number2, number1

if number2 > number3:
    number2, number3 = number3, number2

if number1 > number2:
    number1, number2 = number2, number1

print("The sorted numbers are", number1, number2, number3)
