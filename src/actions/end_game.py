from actions.part_one import first_action
from actions.mechanics import get_user_input
from actions.knock_knock import forest_cabin

'''
def play_again():
    while True:
        path = get_user_input("Do you want to play again? y/n\n")
        if path == "n":
            return "See you later!"
        if path == "y":
            return "Here we go!"
'''

def play_game():
    print(forest_cabin())

