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
    print("You look around and see nothing, what do you do?")
    return get_user_input("You shrug and keep on eating the marshmallows.\nYou put the marshmallow down and look around.\n")
    
    

'''
print(intro())
print(forest_cabin())
'''

