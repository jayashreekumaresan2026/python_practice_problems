def even_odd():
    user_input = int(input("enter the number"))
    if user_input > 0:
        if user_input % 2 == 0:
            print("i am even number")
        else:
            print("i am a odd number")
    else:
        print("please enter the number greater than zero")


even_odd()
