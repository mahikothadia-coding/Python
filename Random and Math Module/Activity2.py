import random
while True:
    user_action = input("Enter one of the following to play rock paper sissors:" \
    "rock, paper, sissors :")

    possible_actions = ["rock", "paper", "sissors"]
    computer_action = random.choice(possible_actions)


    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "sissors":
            print(" You win!")
        else:
            print("You loose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!")
        else:
            print("You have lost the game!")
    elif user_action == "sissors":
        if computer_action == "paper":
            print("You win!")
        else:
            print("You have lost the game!")

    play_again = input("Play again? (y/n): ")
    if play_again == "n":
        break                
                  