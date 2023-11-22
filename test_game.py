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
    

def test_first_action_1():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            first_action()           
        output_lines = captured_output.getvalue().strip().split('\n')
        
    assert len(output_lines) == 6
    assert "You are in the middle of an enchanted forest where your parents left you with some bread" in output_lines[0]
    assert "After walking for a while you come across a cabin made of ginger bread and candy." in output_lines[1]
    assert "You are suspicious, but you are also tired and hungry." in output_lines[2]
    assert "What do you do?" in output_lines[3]
    assert "Enter 1 to knock on the door." in output_lines[4]
    assert "Enter 2 to pick whatever you can grab." in output_lines[5]
  

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


def test_garden_picking():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            garden_picking()           
        output_lines = captured_output.getvalue().strip().split('\n')
        
    assert len(output_lines) == 8
    assert "You take care to hide amongst the bushes and try to stay aware of your surroundings and the cabin." in output_lines[0]
    assert "After a while of nothing happening you decide to start picking up as much candy as you can and fit it in your pockets." in output_lines[1]
    assert "You reach a marshmallow pad. You love marshmallows!" in output_lines[2]
    assert "You decide to have some right there and then, after all, your pockets are getting full and heavy and you need to keep your sugar levels up." in output_lines[3]
    assert "Do not eat that!” a little voice says" in output_lines[4]
    assert "You look around and see nothing, what do you do?" in output_lines[5]
    assert "You shrug and keep on eating the marshmallows." in output_lines[6]
    assert "You put the marshmallow down and look around." in output_lines[7]


def test_garden_picking_input():
    """test user input from garden picking choices"""
    with patch("builtins.input", side_effect=["1"]):
        result = garden_picking()
    assert result == "1"