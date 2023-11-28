from actions import *
from actions.part_one import *
#from actions.knock_knock import *
from actions.garden import *
from actions.end_game import *


def main():
    #print(first_action())
    #print(forest_cabin())
    #rwat = forest_cabin()
    #print(rwat)
    #if rwat == "Here we go!":
    #   print(forest_cabin())
    play_again = True
    while play_again:
        game = play_game()
        play_again_input = get_user_input("Do you want to play again? y/n\n")
        play_again = play_again_input == "y"
    print("See you!")




if __name__ == "__main__":
    main()