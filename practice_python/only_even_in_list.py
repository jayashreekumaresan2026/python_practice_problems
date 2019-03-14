def even_list():
    final_list = []
    user_input = input("enter the list")
    list_values = user_input.split()
    for i in range(0, len(list_values)):
        if int(list_values[i]) % 2 == 0:
            final_list.append(list_values[i])
    print(final_list)


even_list()
