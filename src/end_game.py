from src.part_one import *


def play_again():
    while True:
        path = get_user_input("Do you want to play again? y/n\n")
        if path == "n":
            return "See you later!"
        if path == "y":
            return first_action()