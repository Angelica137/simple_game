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
    return "What do you do?"


def first_choices() -> str:
    """Collects user input from first action"""
    return get_user_input("Enter 1 to knock on the door.\nEnter 2 to pick whatever you can grab.\n")


def forest_cabin() -> str:
    """Collects user action from first action and moves on to next action"""
    while True:
        path = first_choices()
        if path == '1':
            return cabin_knock()
        if path == '2':
            return garden_picking()


def cabin_knock() -> str:
    """Lists the possible outcomes form knocking on the cabin"""
    knock_outcomes = [
        "A young man opens the door.", 
        "No one answers.", 
        "You hear a voice from behind the door."
                ]
    return random.choice(knock_outcomes)


def garden_picking() -> str:
    """Lays the story for what happens at the garden and asks for input"""
    print("You take care to hide amongst the bushes and try to stay aware of your surroundings and the cabin.")
    pause()
    print("After a while of nothing happening you decide to start picking up as much candy as you can and fit it in your pockets.")
    pause()
    print("You reach a marshmallow pad. You love marshmallows!")
    pause()
    print("You decide to have some right there and then, after all, your pockets are getting full and heavy and you need to keep your sugar levels up.")
    pause()
    print("“Do not eat that!” a little voice says.")
    pause()
    print("You look around and see a little fairy, what do you do?")
    return marshmallows()


def garden_picking_input():
    """Gives the user choices for the garden action"""
    return get_user_input("Enter 1 to shrug and keep on eating the marshmallows.\nEnter 2 to start talking to the fairy\n")


def fairy_outcomes_lose() -> str:
    print("You shrug and keep on eating. She is so tiny, and you are so hungry.")
    pause()
    print("“No wait!” you hear the little fairy scream, and then, it all goes black. You are dead :(")
    pause()
    return "GAME OVER.\nDo you want to play again? y/n"


def marshmallows() -> str:
    """Outcomes from action choices at the garden"""
    while True:
        path = garden_picking_input()
        if path == "1":
            return fairy_outcomes_lose()
        if path == "2":
            return fairy_outcomes_win()


def fairy_outcomes_win() -> str:
    print("Hello little fairy! I did not mean to steal these from you.")
    pause()
    print("“You are not stealing from me. you are stealing from him!” She says angrily while pointing her tiny finger behind you.")
    pause()
    print("You turn around and see a large ogre ready to hit you with a huge club.")
    pause()
    print("You dodge the ogre and see him smash the little fairy. You grab your pockets full of candy and run for your life!")
    pause()
    print("You run as fast as you can and before you know it you are out of the forest. There are some lumberjacks about to go in and you fall to your knees and try to tell them there is an ogre, but you are making no sense.")
    pause()
    print("You turn around nervously pointing at the forest.")
    pause()
    print("“Ogre!” finally you manage the words as the ogre makes it out of the forest finally catching up.")
    pause()
    print("The lumberjacks see him and launch an attack on the ogre leaving you on the ground with some candy still in your pockets.")
    return "YOU WIN!\nDo you want to play again? y/n"


#print(intro())
#print(first_action())
#print(forest_cabin())
#print(marshmallows())

