from src.one import *
from freezegun import freeze_time
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch



def test_get_user_input(monkeypatch):
    monkeypatch.setattr('src.one.get_user_input', lambda _: 'Ana')
    result = get_user_input("Welcome, player 1. What is your name?\n")
    assert result == 'Ana'


def test_intro(monkeypatch, capfd):
    monkeypatch.setattr('src.one.get_user_input', lambda _: 'Ana')
    with capfd.disabled():
        result = intro()
    assert result == 'Hi, Ana.'


def test_pause():
    with freeze_time("2022-01-01 00:00:00"):
        result = pause()       
    assert result == time.sleep(2)


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