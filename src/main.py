from actions import *
from actions.part_one import *
from actions.garden import *
from actions.end_game import *


def main():
    play_again = True
    while play_again:
        game = play_game()
        play_again_input = get_user_input("Do you want to play again? y/n\n")
        play_again = play_again_input == "y"
    print("See you later!")




if __name__ == "__main__":
    main()