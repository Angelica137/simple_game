from .mechanics import *


def intro() -> str:
    """Print intro statement and collect user input"""
    name = input("Welcome, player 1. What is your name?\n")
    return (f"Hi, {name}.")


first_act = [
    "You are in the middle of an enchanted forest where your parents left you \
with some bread.",
    "After walking for a while you come across a cabin made of ginger bread \
and candy.",
    "You are suspicious, but you are also tired and hungry."
]


def first_action() -> str:
    """Print first action using story_telling()"""
    return story_telling(first_act, "continue")


def first_choices() -> str:
    """Collects user input from first action"""
    return input("Enter 1 to knock on the door.\nEnter 2 to pick whatever you \
can grab.\n")
