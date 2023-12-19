from .mechanics import *
from .part_one import *
from .garden import garden_picking
from .play_game import *
import random


def forest_cabin() -> str:
    """Collects user input from first action and moves on to next action"""
    while True:
        path = first_choices()
        if path == '1':
            return cabin_knock()
        if path == '2':
            return garden_picking()


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
    "He is putting on his jacket and seems surprised to see you standing \
there. Did he not hear you knocking?",
    "“Hey! who are you?” he asks",
    "“I am… I… my dad left me a while a go in the forest and now I am lost.”",
    "He looks around maybe looking to check that indeed you were alone. He \
looks down at you but you do not know what to make of it.",
    "“I am leaving now, and I have nothing for you to steal so be on your \
way”",
    "You start crying.",
    "“Look, I cannot jut let in some random kid from the forest, you could be \
a vampire for all I know. If you want water the well is over there. If \
you want to sleep you can sleep with the sheep but you better not kill \
them!”",
    "He hands you a handkerchief and moves past you.",
    "“And do steal any of the candy either!”",
    "You make your way to the well, and get some water and then move towards \
the ship pen.",
    "You pick a spot to fall a sleep on the hay.",
    "All of a sudden you see some read eyes in front of you. VAMPIRE!",
]


def man_opens_door():
    return (story_telling(cabin_man, "lose"))


voice = [
    "You slowly enter the cabin",
    "You see an old lady by the kitchen stirring a pot",
    "“Who are you child, what do you want?”",
    "You explain your dad left you in the forest and never came back for you.",
    "She looks at you and asks for your dads name.",
    "“I know old Jack. Sit, you should have something to eat. We will go look \
    for your dad after you eat”",
    "“I do not think my dad wants me back”. You say while having some soup.",
    "“No, I do not imagine he does. You can stay here with me if you are \
    willing to work and learn.”",
    "You slowly nod. And you live happily ever after."
]


def voice_answers():
    return (story_telling(voice, "win"))


def no_answer():
    while True:
        path = input("Enter 1 to enter the house.\nEnter 2 to go to the \
                      garden.\n")
        if path == "1":
            return "You enter the house"
        if path == "2":
            return garden_picking()


go_inside_story = [
        "You go into the house and see the cabin is empty.",
        "The oven apears to be on.",
        "You move towards it slowly and grab some bread for the table and \
        mindlessly start eating it.",
        "You slowly approach the oven to see what is cooking.",
        "You hear some noise from behind you and before you know it… someone \
        shoved you into the oven!"
    ]


def go_into_cabin():
    return (story_telling(go_inside_story, "win"))
