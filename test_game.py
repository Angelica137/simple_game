from game import *
from freezegun import freeze_time
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
import random

'''
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
    

def test_first_action_story():
    """Test the print statements of this function"""
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            first_action()           
        output_lines = captured_output.getvalue().strip().split('\n')
        
    assert len(output_lines) == 3
    assert "You are in the middle of an enchanted forest where your parents left you with some bread" in output_lines[0]
    assert "After walking for a while you come across a cabin made of ginger bread and candy." in output_lines[1]
    assert "You are suspicious, but you are also tired and hungry." in output_lines[2]


def test_first_action_return():
    """Tests this function return statement"""
    result = first_action()
    assert result == "What do you do?"


def test_first_choices_user_input_1():
    """test user input from fisrt_choices() is captured"""
    with patch("builtins.input", side_effect=["1"]):
        result = first_choices()
    assert result == "1"


def test_forest_cabin_path_1_knock_on_door():
    """Asks the user for a choice at the cabin - path knock on door"""
    with patch("game.first_action", return_value='1'), \
    patch('game.random.choice', return_value='A young man opens the door.'):
        result = forest_cabin()
    assert result == 'A young man opens the door.'


def test_forest_cabin_path_2_go_to_garden():
    """Asks the user for a choice at the cabin - path go to garden"""
    with patch("game.forest_cabin", side_effect=["2"]):
        result = forest_cabin()
    assert result == garden_picking()


def test_forest_cabin_path_other():
    """Asks the user for a choice at the cabin - path not 1 or 2"""
    with patch("game.first_action", side_effect=["4", "2"]):
        result = forest_cabin()
    assert result == garden_picking()


def test_cabin_knock(monkeypatch):
    """Retunrs a value from the list"""
    monkeypatch.setattr(random, 'choice', lambda seq: seq[0])
    result = cabin_knock()
    assert result == "A young man opens the door."


def test_garden_picking_path_1():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            garden_picking()           
        output_lines = captured_output.getvalue().strip().split('\n')        
    assert len(output_lines) == 10
    assert "You take care to hide amongst the bushes and try to stay aware of your surroundings and the cabin." in output_lines[0]
    assert "After a while of nothing happening you decide to start picking up as much candy as you can and fit it in your pockets." in output_lines[1]
    assert "You reach a marshmallow pad. You love marshmallows!" in output_lines[2]
    assert "You decide to have some right there and then, after all, your pockets are getting full and heavy and you need to keep your sugar levels up." in output_lines[3]
    assert "Do not eat that!” a little voice says." in output_lines[4]
    assert "You look around and see a little fairy, what do you do?" in output_lines[5]


def test_garden_picking_path_2():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            garden_picking()           
        output_lines = captured_output.getvalue().strip().split('\n')        
    assert len(output_lines) == 16
    assert "You take care to hide amongst the bushes and try to stay aware of your surroundings and the cabin." in output_lines[0]
    assert "After a while of nothing happening you decide to start picking up as much candy as you can and fit it in your pockets." in output_lines[1]
    assert "You reach a marshmallow pad. You love marshmallows!" in output_lines[2]
    assert "You decide to have some right there and then, after all, your pockets are getting full and heavy and you need to keep your sugar levels up." in output_lines[3]
    assert "Do not eat that!” a little voice says." in output_lines[4]
    assert "You look around and see a little fairy, what do you do?" in output_lines[5]
'''

def test_garden_picking_return_statement():
    result = garden_picking()
    assert result == marshmallows()

'''
def test_garden_picking_input():
    """test user input from garden picking choices"""
    with patch("builtins.input", side_effect=["1"]):
        result = garden_picking_input()
    assert result == "1"


def test_marshmallows_1(): #THIS IS FAILING!!!
    """test user stops eating"""
    with patch("builtins.input", side_effect=["1"]):
        result = marshmallows()
    assert result == "You start crawling backwards, slowly."


def test_marshmallows_2(): #THIS IS FAILING!!!
    """test user talks to fairy"""
    with patch("builtins.input", side_effect=["2"]):
        result = marshmallows()
    assert result == "Hello little fairy! I did not mean to steal these from you."


def test_fairy_outcomes_lose(): #THIS IS FAILING!!!
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            fairy_outcomes_lose()           
        output_lines = captured_output.getvalue().strip().split('\n')        
    assert len(output_lines) == 2
    assert "You start crawling backwards, slowly." in output_lines[0]
    assert "“No wait!” you hear the little fairy scream, and then, it all goes black. You are dead :(" in output_lines[1]


def test_fairy_outcomes_lose_return_statement(): #THIS IS FAILING!!!
    result = fairy_outcomes_lose()
    assert result == "GAME OVER."


def test_fairy_outcomes_win():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            fairy_outcomes_win()
        output_lines = captured_output.getvalue().strip().split('\n')
    
    assert len(output_lines) == 8
    assert "Hello little fairy! I did not mean to steal these from you." in output_lines[0]
    assert "“you are not stealing from me. you are stealing from him!” She says angrily while pointing her tiny finger behind you." in output_lines[1]
    assert "You turn around and see a large oar ready to hit you with a huge club." in output_lines[2]
    assert "You dodge the ogre and see him smash the little fairy. You grab your pockets full of candy and run for your life!" in output_lines[3]
    assert "You run as fast as you can and before you know it you are out of the forest. There are some lumberjacks about to go in and you fall to your knees and try to tell them there is an ogre, but you are making no sense." in output_lines[4]
    assert "You turn around nervously pointing at the forest." in output_lines[5]
    assert "“Ogre!” finally you manage the words as the ogre makes it out of the forest finally catching up." in output_lines[6]
    assert "The lumberjacks see him and launch an attack on the ogre leaving you on the ground with some candy still i your pockets." in output_lines[7]


def test_fairy_outcomes_two_return_statement():
    result = fairy_outcomes_win()
    assert result == "YOU WIN!"
    '''