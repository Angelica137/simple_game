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


def first_action() -> str:
    """Print first action"""
    print("You are in the middle of an enchanted forest where your parents left you with some bread")
    pause()
    print("After walking for a while you come across a cabin made of ginger bread and candy.")
    pause()
    print("You are suspicious, but you are also tired and hungry.")    
    pause()
    return ("What do you do?")


def first_choices():
    """Collects user input from first action"""
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
    """Lists the possible outcomes form knocking on the cabin"""
    knock_outcomes = [
        "A young man opens the door.", 
        "No one answers.", 
        "You hear a voice from behind the door."
                ]
    return random.choice(knock_outcomes)


def garden_picking() -> str:
    print("You take care to hide amongst the bushes and try to stay aware of your surroundings and the cabin.")
    pause()
    print("After a while of nothing happening you decide to start picking up as much candy as you can and fit it in your pockets.")
    pause()
    print("You reach a marshmallow pad. You love marshmallows!")
    pause()
    print("You decide to have some right there and then, after all, your pockets are getting full and heavy and you need to keep your sugar levels up.")
    pause()
    print("Do not eat that!” a little voice says")
    pause()
    return "You look around and see a little fairy, what do you do?"


def garden_picking_input():
    return get_user_input("1. You shrug and keep on eating the marshmallows.\n2. Start talking to the fairy\n")


def marshmallows() -> str:
    while True:
        path = garden_picking_input()
        if path == "1":
            return "You start crawling backwards, slowly."
        if path == "2":
            return "WIN"


'''
print(intro())
print(forest_cabin())
'''

