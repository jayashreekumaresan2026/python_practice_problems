def common_element():
    final_list = []
    user_list1 = input("enter the  first list:")
    list1 = user_list1.split()
    user_list2 = input("enter the second list:")
    list2 = user_list2.split()
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                final_list.append(list2[j])
    result = set(final_list)
    print(result)


common_element()
