from src.actions.mechanics import *
from freezegun import freeze_time
from unittest.mock import patch
from builtins import StopIteration

'''
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


def test_choices_path_1():
    """tests the user is given choices and moves the game"""
    mock_options = {"prompt": "enter 1 or 2",
                    "1": lambda: "1 is valid",
                    "2": lambda: "is valid too"}
    with patch("builtins.input", side_effect=["1"]):
        result = choices(mock_options)
    assert result == "1 is valid"


def test_choices_path_2():
    """tests the user is given choices and moves the game"""
    mock_options = {"prompt": "enter 1 or 2",
                    "1": lambda: "1 is valid",
                    "2": lambda: "is valid too"}
    with patch("builtins.input", side_effect=["2"]):
        result = choices(mock_options)
    assert result == "is valid too"



class InvalidChoiceError(Exception):
    pass


def test_invalid_input(capsys, monkeypatch):
    """Tests the 'else' statement in the choices function"""
    # Mock the input function to return an invalid choice
    monkeypatch.setattr('builtins.input', lambda _: '3')

    mock_options = {"prompt": "Enter 1 or 2",
                    "1": lambda: "Option 1 chosen",
                    "2": lambda: "Option 2 chosen"}

    # Monkeypatch the first_choices function to raise InvalidChoiceError after
    # one iteration
    with monkeypatch.context() as m:
        count = 0

        def custom_get_user_input(prompt="Enter your choice: ", sentinel=None):
            nonlocal count
            count += 1
            if count > 1:
                raise InvalidChoiceError("Invalid choice")
            return '3'

        m.setattr('src.actions.mechanics.choices',
                  custom_get_user_input)

    # Call choices
    with pytest.raises(InvalidChoiceError, match="Invalid choice"):
        choices(mock_options)

    # Capture the printed output
    captured_output = capsys.readouterr()

    # Check the expected output
    expected_output = "Oops! invalid_choice is not an option.\n"
    assert captured_output.out == expected_output
'''

