from actions import *
from actions.play_game import *


def main():
    play_again = True
    while play_again:
        game = play_game()
        options = {
                  "prompt": "Do you want to play again? y/n\n",
                  "y": lambda: "y",
                  "n": lambda: "See you later!"
                  }
        path = (choices(options))
        if path == "See you later!":
            print(path)
            break


if __name__ == "__main__":
    main()
