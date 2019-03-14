def prime_number():
    user_input = int(input("enter the number"))
    count = 0
    for i in range(1, user_input+1):
        if user_input % i == 0:
            count = count + 1

    if count == 2:
        print("prime number")
    else:
        print("Not a prime number")


prime_number()
