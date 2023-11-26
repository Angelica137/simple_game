from src.mechanics import *


def intro() -> str:
    """Print intro statement and collect user input"""
    name = get_user_input("Welcome, player 1. What is your name?\n")
    return (f"Hi, {name}.")


first_act = [
    "You are in the middle of an enchanted forest where your parents left you with some bread.",
    "After walking for a while you come across a cabin made of ginger bread and candy.",
    "You are suspicious, but you are also tired and hungry."
]


def first_action() -> str:
    """Print first action using story_telling()"""
    return story_telling(first_act, "continue")


def first_choices() -> str:
    """Collects user input from first action"""
    return get_user_input("Enter 1 to knock on the door.\nEnter 2 to pick whatever you can grab.\n")


def forest_cabin() -> str:
    """Collects user input from first action and moves on to next action"""
    while True:
        path = first_choices()
        if path == '1':
            return cabin_knock()
        if path == '2':
            return garden_picking()