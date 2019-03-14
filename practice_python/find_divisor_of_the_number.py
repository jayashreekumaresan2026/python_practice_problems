def divisor_of_number():
    user_input = int(input("enter the number=>"))
    final_value = []
    for i in range(1, user_input+1):
        if user_input % i == 0:
            final_value.append(i)

    print(final_value)
divisor_of_number()
