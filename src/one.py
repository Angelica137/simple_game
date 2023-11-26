import time


def get_user_input(prompt: str) -> str:
    """Capture user input"""
    return input(prompt)


def intro() -> str:
    """Print intro statement and collect user input"""
    name = get_user_input("Welcome, player 1. What is your name?\n")
    return (f"Hi, {name}.")


def pause() -> int:
    return time.sleep(2)


def story_telling(story: list, outcome: str) -> str:
    for line in story:
        pause()
        print(line)
    return outcome


continue_scene = "What do you do?"
game_over = "GAME OVER."
win = "YOU WIN!"


first_act = [
    "You are in the middle of an enchanted forest where your parents left you with some bread.",
    "After walking for a while you come across a cabin made of ginger bread and candy.",
    "You are suspicious, but you are also tired and hungry."
]


def first_action() -> str:
    """Print first action using story_telling()"""
    return story_telling(first_act, continue_scene)


def first_choices() -> str:
    """Collects user input from first action"""
    return get_user_input("Enter 1 to knock on the door.\nEnter 2 to pick whatever you can grab.\n")
