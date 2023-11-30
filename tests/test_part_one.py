from src.actions.part_one import *
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
import random


def test_intro(monkeypatch, capfd):
    monkeypatch.setattr('src.actions.part_one.intro', lambda _: 'Ana')
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
