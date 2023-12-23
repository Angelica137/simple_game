import time


def pause() -> int:
    return time.sleep(2)


scene_outcomes = {
        "continue": "What do you do?",
        "lose": "GAME OVER.",
        "win": "YOU WIN!"
    }


def story_telling(story: list, outcome: str) -> str:
    for line in story:
        pause()
        print(line)
    return scene_outcomes.get(outcome)


def choices(options: dict) -> str:
    """gives the user an option and moves on the game"""
    while True:
        path = input(options["prompt"])
        if path in options:
            return options[path]()
        else:
            print(f'Oops! {path} is not an option.')
