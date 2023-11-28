import time


def get_user_input(prompt: str) -> str:
    """Capture user input"""
    return input(prompt)


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
    end_scene = scene_outcomes.get(outcome)
    return end_scene


