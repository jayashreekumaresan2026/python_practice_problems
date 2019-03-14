def palindrom_string():
    user_input = input("enter the string")
    print(user_input)
    reverse = user_input[::-1]
    print(reverse)
    if user_input == reverse:
        print('yes')

    else:
        print("no")


palindrom_string()
