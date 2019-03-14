def element_in_list(array, search_element):
    for i in range(0, len(array)):
        if array[i] == search_element:
            print("True")
            break
        else:
            print("False")


array = [1, 2, 3, 4]
search_element = 6
element_in_list(array, search_element)
