import random

l = ["Rock", "Paper", "Scissors"]

def gameLogic(user_input):

    if user_input not in l:
        print("Enter valid choice")
        return

    system_input = l[random.randint(0, 2)]

    print(f"User_input = {user_input}")
    print(f"System_input = {system_input}")

    if user_input == system_input:
        print("Draw")
    elif (user_input == "Rock" and system_input == "Scissors") or \
         (user_input == "Paper" and system_input == "Rock") or \
         (user_input == "Scissors" and system_input == "Paper"):
        print("You WON!")
    else:
        print("You lost")

user_input = input('''Choose any one of the following:
i. Rock
ii. Paper
iii. Scissors
Enter your choice here:  ''')

gameLogic(user_input)
