import time

def get_user_input(prompt) -> str:
    """Capture user input"""
    return input(prompt)

def intro() -> str:
    """Print intro statement and collect user input"""
    return get_user_input("Welcome, player 1. What is your name?: ")

def second_action() -> str:
    """Print second action and collect user input"""
    return get_user_input("Second: ")

def pause() -> int:
    return time.sleep(2)


def long_story() -> str:
    pause()
    paragraph = "this is some long copy"
    return paragraph

'''
print(long_story())
print(long_story())
print(intro())
print(second_action())
'''