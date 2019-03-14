def fibonacci():
    user_input = int(input("Enter the number"))
    first = 0
    second = 1
    print(first)
    print(second)
    for i in range(0,user_input):
        c = first + second
        print(c)
        first = second
        second = c




fibonacci()
