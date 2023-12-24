from .mechanics import *


roam_garden = [
    "You take care to hide amongst the bushes and try to stay aware of your \
surroundings and the cabin.",
    "After a while of nothing happening you decide to start picking up as \
much candy as you can and fit it in your pockets.",
    "You reach a marshmallow pad. You love marshmallows!",
    "You decide to have some right there and then, after all, your pockets \
are getting full and heavy and you need to keep your sugar levels up.",
    "“Do not eat that!” a little voice says.",
    "You look around and see a little fairy.",
]


def garden_picking() -> str:
    """Lays the story for what happens at the garden and asks for input"""
    print(story_telling(roam_garden, "continue"))
    return marshmallows()


keep_eating = [
        "You shrug and keep on eating. She is so tiny, and you are so hungry.",
        "“No wait!” you hear the little fairy scream, and then, it all goes \
black. You are dead :(",
]


def fairy_outcomes_lose() -> str:
    return (story_telling(keep_eating, "lose"))


def marshmallows() -> str:
    """Outcomes from action choices at the garden"""
    options = {"1": fairy_outcomes_lose,
               "2": fairy_outcomes_win,
               "prompt": "Enter 1 to shrug and keep on eating the \
marshmallows.\nEnter 2 to start talking to the fairy.\n"}
    return (choices(options))


fairy = [
    "Hello little fairy! I did not mean to steal these from you.",
    "“You are not stealing from me. you are stealing from him!” She says \
angrily while pointing her tiny finger behind you.",
    "You turn around and see a large ogre ready to hit you with a huge club.",
    "You dodge the ogre and see him smash the little fairy. You grab your \
pockets full of candy and run for your life!",
    "You run as fast as you can and before you know it you are out of the \
forest. There are some lumberjacks about to go in and you fall to your \
knees and try to tell them there is an ogre, but you are making no sense.",
    "You turn around nervously pointing at the forest.",
    "“Ogre!” finally you manage the words as the ogre makes it out of the \
forest finally catching up.",
    "The lumberjacks see him and launch an attack on the ogre leaving you on \
the ground with some candy still in your pockets."
]


def fairy_outcomes_win() -> str:
    return (story_telling(fairy, "win"))
