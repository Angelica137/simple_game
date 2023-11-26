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

'''
def story_telling(story: list, outcome: str) -> str:
    for line in story:
        pause()
        print(line)
    return outcome


continue_scene = "What do you do?"
game_over = "GAME OVER."
win = "YOU WIN!"
'''

scene_outcomes = {
        "continue": "What do you do?",
        "lose": "GAME OVER.",
        "win": "YOU WIN!"
    }


def story_telling(story: list, outcome: str) -> str:
    for line in story:
        pause()
        print(line)
        end_scene = scene_outcomes.get(outcome)
    return end_scene



first_act = [
    "You are in the middle of an enchanted forest where your parents left you with some bread.",
    "After walking for a while you come across a cabin made of ginger bread and candy.",
    "You are suspicious, but you are also tired and hungry."
]


def play():
    print (first_action())
    return forest_cabin()


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


roam_garden = [
    "You take care to hide amongst the bushes and try to stay aware of your surroundings and the cabin.",
    "After a while of nothing happening you decide to start picking up as much candy as you can and fit it in your pockets.",
    "You reach a marshmallow pad. You love marshmallows!",
    "You decide to have some right there and then, after all, your pockets are getting full and heavy and you need to keep your sugar levels up.",
    "“Do not eat that!” a little voice says.",
    "You look around and see a little fairy.",
]


def garden_picking() -> str:
    """Lays the story for what happens at the garden and asks for input"""
    print(story_telling(roam_garden, continue_scene))
    return marshmallows()


def garden_picking_input():
    """Gives the user choices for the garden action"""
    return get_user_input("Enter 1 to shrug and keep on eating the marshmallows.\nEnter 2 to start talking to the fairy.\n")


keep_eating = [
        "You shrug and keep on eating. She is so tiny, and you are so hungry.",
        "“No wait!” you hear the little fairy scream, and then, it all goes black. You are dead :(",
]


def fairy_outcomes_lose() -> str:
    print(story_telling(keep_eating, game_over))
    return play_again()


def marshmallows() -> str:
    """Outcomes from action choices at the garden"""
    while True:
        path = garden_picking_input()
        if path == "1":
            return fairy_outcomes_lose()
        if path == "2":
            return fairy_outcomes_win()


fairy = [
    "Hello little fairy! I did not mean to steal these from you.",
    "“You are not stealing from me. you are stealing from him!” She says angrily while pointing her tiny finger behind you.",
    "You turn around and see a large ogre ready to hit you with a huge club.",
    "You dodge the ogre and see him smash the little fairy. You grab your pockets full of candy and run for your life!",
    "You run as fast as you can and before you know it you are out of the forest. There are some lumberjacks about to go in and you fall to your knees and try to tell them there is an ogre, but you are making no sense.",
    "You turn around nervously pointing at the forest.",
    "“Ogre!” finally you manage the words as the ogre makes it out of the forest finally catching up.",
    "The lumberjacks see him and launch an attack on the ogre leaving you on the ground with some candy still in your pockets."
]


def fairy_outcomes_win() -> str:
    print(story_telling(fairy, win))
    return play_again()


knock_outcomes = [
        "A young man opens the door.", 
        "No one answers.", 
        "You hear a voice from behind the door."
                ]


def cabin_knock() -> str:
    """Lists the possible outcomes form knocking on the cabin"""
    path = random.choice(knock_outcomes)
    print(path)
    if path == knock_outcomes[0]:
        return man_opens_door()
    if path == knock_outcomes[1]:
        return go_into_cabin()
    if path == knock_outcomes[2]:
        return voice_answers()


cabin_man = [
    "He is putting on his jacket and seems surprised to see you standing there. Did he not hear you knocking?",
    "“Hey! who are you?” he asks",
    "“I am… I… my dad left me a while a go in the forest and now I am lost.”",
    "He looks around maybe looking to check that indeed you were alone. He looks down at you but you do not know what to make of it.",
    "“I am leaving now, and I have nothing for you to steal so be on your way”",
    "You start crying.",
    "“Look, I cannot jut let in some random kid from the forest, you could be a vampire for all I know. If you want water the well is over there. If you want to sleep you can sleep with the sheep but you better not kill them!”",
    "He hands you a handkerchief and moves past you.",
    "“And do steal any of the candy either!”",
    "You make your way to the well, and get some water and then move towards the ship pen.",
    "You pick a spot to fall a sleep on the hay.",
    "All of a sudden you see some read eyes in front of you. VAMPIRE!",
]


def man_opens_door():
    print(story_telling(cabin_man, game_over))
    return play_again()


voice = [
    "You slowly enter the cabin",
    "You see an old lady by the kitchen stirring a pot",
    "“Who are you child, what do you want?”",
    "You explain your dad left you in the forest and never came back for you.",
    "She looks at you and asks for your dads name.",
    "“I know old Jack. Sit, you should have something to eat. We will go look for your dad after you eat”",
    "“I do not think my dad wants me back”. You say while having some soup.",
    "“No, I do not imagine he does. You can stay here with me if you are willing to work and learn.”",
    "You slowly nod. And you live happily ever after."
]

def voice_answers():
    print(story_telling(voice, win))
    return play_again()


def no_answer():
    while True:
        path = get_user_input("Enter 1 to enter the house.\nEnter 2 to go to the garden.\n")
        if path == "1":
            return "You enter the house"
        if path == "2":
            return garden_picking()


go_inside_story = [
        "You go into the house and see the cabin is empty.",
        "The oven apears to be on.",
        "You move towards it slowly and grab some bread for the table and mindlessly start eating it.",
        "You slowly approach the oven to see what is cooking.",
        "You hear some noise from behind you and before you know it… someone shoved you into the oven!"
		]


def go_into_cabin():
    return story_telling(go_inside_story, win)


def play_again():
    while True:
        path = get_user_input("Do you want to play again? y/n\n")
        if path == "n":
            return "See you later!"
        if path == "y":
            return first_action()



print(play())

