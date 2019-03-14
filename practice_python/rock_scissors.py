def rock_scissors():
    user_option = input("you want to play game:")
    if user_option == 'yes':
        user_input1 = input("enter the option")
        user_input2 = input("enter the option")

        if user_input1 == user_input2:
            print("game Tie")
        elif (user_input1 == 'scissor' and user_input2 == 'paper') or (
                user_input1 == 'paper' and user_input2 == 'rock') or (
                user_input1 == 'rock' and user_input2 == 'scissor'):

            print("user1 is win.....")
        else:
            print("user2 is win.....")

    else:
        print("THANK FOR YOUR INTEREST")


rock_scissors()
