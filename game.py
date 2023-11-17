import time

def get_user_input(prompt) -> str:
    """Capture user input"""
    return input(prompt)

def intro() -> str:
    """Print intro statement and collect user input"""
    return get_user_input("Q: ")

def second_action() -> str:
    """Print second action and collect user input"""
    return get_user_input("Second: ")

def pause() -> int:
    return time.sleep(2)

#print(intro())
#print(second_action())