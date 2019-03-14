def list_problems():
    user_input = "1 2 3 4 4 2 1"
    list_values = user_input.split()
    user_input_value = 3
    final_list = []
    for i in range(0, len(list_values)):
        if list_values[i] < str(user_input_value):
            final_list.append(list_values[i])
    print(final_list)


list_problems()
