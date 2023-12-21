from src.actions.garden import *
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
import pytest


def test_garden_picking_path_1():
    """Tests choosing to keep eating and stop playing -> does NOT want to
        play. Enter 1 then n."""
    with patch("builtins.input", side_effect=["1", "n"]), \
            StringIO() as captured_output:
        with redirect_stdout(captured_output):
            garden_picking()
        output_lines = captured_output.getvalue().strip().split('\n')

    assert len(output_lines) == 9
    assert "You take care to hide amongst the bushes and try to stay aware \
of your surroundings and the cabin." in output_lines[0]
    assert "After a while of nothing happening you decide to start picking \
up as much candy as you can and fit it in your pockets." in output_lines[1]
    assert "You reach a marshmallow pad. You love \
marshmallows!" in output_lines[2]
    assert "You decide to have some right there and then, after all, your \
pockets are getting full and heavy and you need to keep your sugar levels \
up." in output_lines[3]
    assert "Do not eat that!” a little voice says." in output_lines[4]
    assert "You look around and see a little fairy." in output_lines[5]
    assert "What do you do?" in output_lines[6]
    assert "You shrug and keep on eating. She is so tiny, and you are so \
hungry." in output_lines[7]
    assert "“No wait!” you hear the little fairy scream, and then, it all \
goes black. You are dead :(" in output_lines[8]


def test_garden_picking_path_2():
    """Tests using choosing to talk to the fairy -> does NOT want to play.
        Enter 2 then n."""
    with patch("builtins.input", side_effect=["2", "n"]), \
            StringIO() as captured_output:
        with redirect_stdout(captured_output):
            garden_picking()
        output_lines = captured_output.getvalue().strip().split('\n')
    assert len(output_lines) == 15
    assert "You take care to hide amongst the bushes and try to stay aware of \
your surroundings and the cabin." in output_lines[0]
    assert "After a while of nothing happening you decide to start picking up \
as much candy as you can and fit it in your pockets." in output_lines[1]
    assert "You reach a marshmallow pad. You love \
marshmallows!" in output_lines[2]
    assert "You decide to have some right there and then, after all, your \
pockets are getting full and heavy and you need to keep your sugar levels \
up." in output_lines[3]
    assert "Do not eat that!” a little voice says." in output_lines[4]
    assert "You look around and see a little fairy." in output_lines[5]


def test_garden_picking_return_statement():
    with patch("builtins.input", side_effect=["2", "2"]):
        result = garden_picking()
    assert result == "YOU WIN!"


def test_garden_picking_input():
    """test user input from garden picking choices"""
    with patch("builtins.input", side_effect=["1"]):
        result = garden_picking_input()
    assert result == "1"


def test_marshmallows_1():
    """test user stops eating and wants to stop playing"""
    with patch("builtins.input", side_effect=["1", "n"]):
        result = marshmallows()
    assert result == "GAME OVER."


def test_marshmallows_2():
    """test user talks to fairy"""
    with patch("builtins.input", side_effect=["2", "n"]):
        result = marshmallows()
    assert result == "YOU WIN!"


def test_fairy_outcomes_lose():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            fairy_outcomes_lose()
        output_lines = captured_output.getvalue().strip().split('\n')
    assert len(output_lines) == 2
    assert "You shrug and keep on eating. She is so tiny, and you are \
so hungry." in output_lines[0]
    assert "“No wait!” you hear the little fairy scream, and then, it \
all goes black. You are dead :(" in output_lines[1]


def test_fairy_outcomes_lose_return_statement():
    """Test return statement from loosing outcome at fairy"""
    with patch("builtins.input", side_effect=["n"]):
        result = fairy_outcomes_lose()
    assert result == "GAME OVER."


def test_fairy_outcomes_win():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            fairy_outcomes_win()
        output_lines = captured_output.getvalue().strip().split('\n')

    assert len(output_lines) == 8
    assert "Hello little fairy! I did not mean to steal these from \
you." in output_lines[0]
    assert "“You are not stealing from me. you are stealing from him!” \
She says angrily while pointing her tiny finger behind you." in output_lines[1]
    assert "You turn around and see a large ogre ready to hit you with a huge \
club." in output_lines[2]
    assert "You dodge the ogre and see him smash the little fairy. You grab \
your pockets full of candy and run for your life!" in output_lines[3]
    assert "You run as fast as you can and before you know it you are out \
of the forest. There are some lumberjacks about to go in and you fall to your \
knees and try to tell them there is an ogre, but you are making no \
sense." in output_lines[4]
    assert "You turn around nervously pointing at the forest\
." in output_lines[5]
    assert "“Ogre!” finally you manage the words as the ogre makes it out of \
the forest finally catching up." in output_lines[6]
    assert "The lumberjacks see him and launch an attack on the ogre leaving \
you on the ground with some candy still in your pockets." in output_lines[7]


def test_fairy_outcomes_two_return_statement():
    with patch("builtins.input", side_effect=["n"]):
        result = fairy_outcomes_win()
    assert result == "YOU WIN!"


class InvalidChoiceError(Exception):
    pass


def test_invalid_choice(capsys, monkeypatch):
    """Tests input validation return statement"""
    # Mock the input function to return '3'
    monkeypatch.setattr('builtins.input', lambda _: '3')

    # Monkeypatch the first_choices function to raise InvalidChoiceError after
    # one iteration
    with monkeypatch.context() as m:
        count = 0

        def custom_garden_picking_input(prompt="Enter your choice: ",
                                        sentinel=None):
            nonlocal count
            count += 1
            if count > 1:
                raise InvalidChoiceError("Invalid choice")
            return '3'

        m.setattr('src.actions.garden.garden_picking_input',
                  custom_garden_picking_input)

        # Call marshmallows
        with pytest.raises(InvalidChoiceError, match="Invalid choice"):
            marshmallows()

    # Capture the printed output
    captured_output = capsys.readouterr()

    # Check the expected output
    expected_output = "Oops! 3 is not an option.\n"
    assert captured_output.out == expected_output
