import time


def get_user_input(prompt: str) -> str:
    """Capture user input"""
    return input(prompt)


def pause() -> int:
    return time.sleep(2)


def story_telling(story: list, outcome: str) -> str:
    for line in story:
        pause()
        print(line)
    return outcome