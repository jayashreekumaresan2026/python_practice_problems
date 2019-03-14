def guess_the_number():
    guess_number = 5
    count = 0
    if guess_number != 'exit':
        count = count + 1
        user_number = int(input("guess your number:"))
        if user_number == guess_number:
            print("Wow your number is correct")
        elif user_number > guess_number:
            print("your number is greater the guess number")
        elif user_number < guess_number:
            print("your number is less the guess number")
    else:
        print("you want to exit ")
    print(count)


guess_the_number()
