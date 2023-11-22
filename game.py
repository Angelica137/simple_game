import time, random

def get_user_input(prompt: str) -> str:
    """Capture user input"""
    return input(prompt)


def intro() -> str:
    """Print intro statement and collect user input"""
    name = get_user_input("Welcome, player 1. What is your name?\n")
    return (f"Hi, {name}.")


def pause() -> int:
    return time.sleep(2)


def long_story() -> str:
    """Print the intro the game"""
    print("You are in the middle of an enchanted forest where your parents left you with some bread")
    pause()
    print("After walking for a while you come across a cabin made of ginger bread and candy.")
    pause()
    print("You are suspicious, but you are also tired and hungry.")
    pause()
    return "What do you do?"


def first_action() -> str:
    """Print first action and collect user input"""
    print("You are in the middle of an enchanted forest where your parents left you with some bread")
    pause()
    print("After walking for a while you come across a cabin made of ginger bread and candy.")
    pause()
    print("You are suspicious, but you are also tired and hungry.")    
    pause()
    print("What do you do?")
    return get_user_input("Enter 1 to knock on the door.\nEnter 2 to pick whatever you can grab.\n")


def forest_cabin() -> str:
    """Collects user action from first action and moves on to next action"""
    while True:
        path = first_action()
        if path == '1':
            return cabin_knock()
        if path == '2':
            return "You go into stealth mode and move around the property towards the nearest candy bush."


def cabin_knock() -> str:
    knock_outcomes = [
        "A young man opens the door.", 
        "No one answers.", 
        "A woman opens the door."
                ]
    return random.choice(knock_outcomes)
    

'''
print(intro())
print(long_story())
print(forest_cabin())
'''

