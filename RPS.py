# import randint from 'random' module
from random import randint

"""
Codecademy - Learn Python 2
Rock, Paper, Scissors
Nasim Ahmed
"""

# create list of options to choose from
options = ["ROCK", "PAPER", "SCISSORS"]

message = {
    "tie": "Yawn it's a tie!",
    "won": "Yay you won!",
    "lost": "Aww you lost!"
}


def decide_winner(user_choice, computer_choice):
    print("User selected: %s" % user_choice)
    print("Computer selected: %s" % computer_choice)

    if user_choice == computer_choice:
        print(message["tie"])
    elif user_choice == options[0] and computer_choice == options[2]:
        print("%s beats %s" % (user_choice, computer_choice))
        print(message["won"])
    elif user_choice == options[1] and computer_choice == options[0]:
        print("%s beats %s" % (user_choice, computer_choice))
        print(message["won"])
    elif user_choice == options[2] and computer_choice == options[1]:
        print("%s beats %s" % (user_choice, computer_choice))
        print(message["won"])
    else:
        print("%s beats %s" % (computer_choice, user_choice))
        print(message["lost"])


def play_RPS():
    user_choice = input("Enter Rock, Paper, or Scissors: ")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)


play_RPS()
