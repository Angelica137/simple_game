from actions.part_one import first_action
from actions.mechanics import get_user_input


def play_again():
    while True:
        path = get_user_input("Do you want to play again? y/n\n")
        if path == "n":
            return "See you later!"
        if path == "y":
            return first_action()


#print(play_again())
