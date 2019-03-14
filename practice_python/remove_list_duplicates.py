def remove_duplicates():
    array = []
    user_input = input("enter the list")
    list_items = user_input.split()
    for i in range(0, len(list_items)):
        if list_items[i] not in array:
            array.append(list_items[i])
    print(array)


remove_duplicates()
