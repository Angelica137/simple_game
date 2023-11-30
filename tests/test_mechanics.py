from src.actions.mechanics import *
from freezegun import freeze_time
from unittest.mock import patch, call



def test_pause():
    with freeze_time("2022-01-01 00:00:00"):
        result = pause()       
    assert result == time.sleep(2)


def test_story_telling():
    with patch('builtins.print') as mock_print:
        story = ["1", "something else", "something other"]
        outcome = "win"
        result = story_telling(story, outcome)
        mock_print.assert_has_calls([
            call("1"),
            call("something else"),
            call("something other")
				])

        assert result == "YOU WIN!"