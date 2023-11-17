import time

def get_user_input(prompt) -> str:
    """Capture user input"""
    return input(prompt)


def intro() -> str:
    """Print intro statement and collect user input"""
    return get_user_input("Welcome, player 1. What is your name?: ")


def pause() -> int:
    return time.sleep(2)


def long_story() -> str:
    print("You are in the middle of an enchanted forest where your parents left you with some bread")
    pause()
    print("After walking for a while you come across a cabin made of ginger bread and candy.")
    pause()
    print("You are suspicious, but you are also tired and hungry.")
    return pause()


def first_action() -> str:
    """Print first action and collect user input"""
    return get_user_input("What do you do do? \n Enter 1 to knock on the door. \nEnter 2 to pick whatever you can grab.")


'''
print(intro())
print(long_story())
print(first_action())
'''