def maximum_number(number1, number2, number3):
    if number1 > number2 or number1 > number3:
        print("Number1 is bigger")
    elif number2 > number1 or number2 > number3:
        print("Number2 is bigger")
    else:
        print("Number4 is bigger")


number1 = 4
number2 = 6
number3 = 8

maximum_number(number1, number2, number3)
