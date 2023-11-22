from game import *
from freezegun import freeze_time
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
import random

def test_get_user_input(monkeypatch):
    monkeypatch.setattr('game.get_user_input', lambda _: 'Ana')
    result = get_user_input("Welcome, player 1. What is your name?\n")
    assert result == 'Ana'


def test_intro(monkeypatch, capfd):
    monkeypatch.setattr('game.get_user_input', lambda _: 'Ana')
    # Redirect stdout to capfd
    with capfd.disabled():
        result = intro()
    assert result == 'Hi, Ana.'


def test_pause():
    with freeze_time("2022-01-01 00:00:00"):
        result = pause()       
    assert result == time.sleep(2)
    

def test_first_action_user_input_1():
    """test user input from fisrt action is captured"""
    with patch("builtins.input", side_effect=["1"]):
        result = first_action()
    assert result == "1"
    

def test_forest_cabin_path_2():
    with patch("game.first_action", side_effect=["2"]):
        result = forest_cabin()
    assert result == "You go into stealth mode and move around the property towards the nearest candy bush."


def test_forest_cabin_path_other():
    with patch("game.first_action", side_effect=["4", "2"]):
        result = forest_cabin()
    assert result == "You go into stealth mode and move around the property towards the nearest candy bush."


def test_cabin_knock(monkeypatch):
    """Test the user gets a result from the list of possible results.
        this test is deterministic."""
    monkeypatch.setattr(random, 'choice', lambda seq: seq[0])
    result = cabin_knock()
    assert result == "A young man opens the door."


def test_forest_cabin_path_1():
    with patch("game.first_action", return_value='1'), \
    patch('game.random.choice', return_value='A young man opens the door.'):
        result = forest_cabin()
    assert result == 'A young man opens the door.'