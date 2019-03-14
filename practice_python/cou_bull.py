import random


def cow_bull():
    random_number = str(random.randint(1000, 9999))
    array = []
    cow = 0
    for i in random_number:
        array.append(i)
    print(array)
    while cow < 4:
        user_value = input("enter your choice  4 digit number ")
        user_input = []
        cow = 0
        bull = 0
        for i in user_value:
            user_input.append(i)
        for i in array:
            if i in user_input and array.index(i) == user_input.index(i):
                cow += 1
            if i in user_input and array.index(i) != user_input.index(i):
                bull += 1
        print(cow, "cow(s)", bull, "bull(s)")

    print(array, user_input)


cow_bull()
