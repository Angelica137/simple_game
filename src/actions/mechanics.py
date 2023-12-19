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
