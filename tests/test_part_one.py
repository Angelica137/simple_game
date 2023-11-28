from src.part_one import *
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
import random
from src.end_game import *

'''
def test_intro(monkeypatch, capfd):
    monkeypatch.setattr('src.part_one.get_user_input', lambda _: 'Ana')
    with capfd.disabled():
        result = intro()
    assert result == 'Hi, Ana.'


def test_first_action_story():
    """Test the print statements of this function"""
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            first_action()           
        output_lines = captured_output.getvalue().strip().split('\n')
    assert len(output_lines) == 3
    assert "You are in the middle of an enchanted forest where your parents left you with some bread." in output_lines[0]
    assert "After walking for a while you come across a cabin made of ginger bread and candy." in output_lines[1]
    assert "You are suspicious, but you are also tired and hungry." in output_lines[2]


def test_first_action_return_statement():
    """Test first action returns string"""
    result = first_action()
    assert result == "What do you do?"


def test_first_choices_user_input_1():
    """test user input from first_choices() is captured"""
    with patch("builtins.input", side_effect=["1"]):
        result = first_choices()
    assert result == "1"
'''

def test_forest_cabin_path_1_knock_on_door():
    """Asks the user for a choice at the cabin - path knock on door.
        Do not play again."""
    with patch("src.part_one.first_action", return_value='1'), \
    patch('random.choice', return_value='A young man opens the door.'):
        result = forest_cabin()
    assert result == "See you later!"

'''
def test_forest_cabin_path_2_go_to_garden():
    """Asks the user for a choice at the cabin - path go to garden"""
    with patch("src.part_one.forest_cabin", side_effect=["2"]):
        result = forest_cabin()
    assert result == garden_picking()


def test_forest_cabin_path_other():
    """Asks the user for a choice at the cabin - path not 1 or 2"""
    with patch("src.part_one.first_action", side_effect=["4", "2"]):
        result = forest_cabin()
'''