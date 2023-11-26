from src.game import *
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
    """Tests using choosing to keep eating and stop playing"""
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            garden_picking()           
        output_lines = captured_output.getvalue().strip().split('\n')        
    assert len(output_lines) == 13
    assert "You take care to hide amongst the bushes and try to stay aware of your surroundings and the cabin." in output_lines[0]
    assert "After a while of nothing happening you decide to start picking up as much candy as you can and fit it in your pockets." in output_lines[1]
    assert "You reach a marshmallow pad. You love marshmallows!" in output_lines[2]
    assert "You decide to have some right there and then, after all, your pockets are getting full and heavy and you need to keep your sugar levels up." in output_lines[3]
    assert "Do not eat that!” a little voice says." in output_lines[4]
    assert "You look around and see a little fairy." in output_lines[5]


def test_garden_picking_path_2():
    """Tests using choosing to talk to the fairy"""
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            garden_picking()           
        output_lines = captured_output.getvalue().strip().split('\n')        
    assert len(output_lines) == 19
    assert "You take care to hide amongst the bushes and try to stay aware of your surroundings and the cabin." in output_lines[0]
    assert "After a while of nothing happening you decide to start picking up as much candy as you can and fit it in your pockets." in output_lines[1]
    assert "You reach a marshmallow pad. You love marshmallows!" in output_lines[2]
    assert "You decide to have some right there and then, after all, your pockets are getting full and heavy and you need to keep your sugar levels up." in output_lines[3]
    assert "Do not eat that!” a little voice says." in output_lines[4]
    assert "You look around and see a little fairy." in output_lines[5]


def test_garden_picking_return_statement():
    result = garden_picking()
    assert result == marshmallows()


def test_garden_picking_input():
    """test user input from garden picking choices"""
    with patch("builtins.input", side_effect=["1"]):
        result = garden_picking_input()
    assert result == "1"


def test_marshmallows_1():
    """test user stops eating and wants to stop playing"""
    with patch("builtins.input", side_effect=["1", "n"]):
        result = marshmallows()
    assert result == "See you later!"


def test_marshmallows_2():
    """test user talks to fairy"""
    with patch("builtins.input", side_effect=["2", "n"]):
        result = marshmallows()
    assert result == "See you later!"


def test_fairy_outcomes_lose():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            fairy_outcomes_lose()           
        output_lines = captured_output.getvalue().strip().split('\n')        
    assert len(output_lines) == 4
    assert "You shrug and keep on eating. She is so tiny, and you are so hungry." in output_lines[0]
    assert "“No wait!” you hear the little fairy scream, and then, it all goes black. You are dead :(" in output_lines[1]


def test_fairy_outcomes_lose_return_statement():
    """Test return statement from loosing outcome at fairy"""
    with patch("builtins.input", side_effect=["n"]):
        result = fairy_outcomes_lose()
    assert result == "See you later!"


	
def test_fairy_outcomes_win():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            fairy_outcomes_win()
        output_lines = captured_output.getvalue().strip().split('\n')
    
    assert len(output_lines) == 10
    assert "Hello little fairy! I did not mean to steal these from you." in output_lines[0]
    assert "“You are not stealing from me. you are stealing from him!” She says angrily while pointing her tiny finger behind you." in output_lines[1]
    assert "You turn around and see a large ogre ready to hit you with a huge club." in output_lines[2]
    assert "You dodge the ogre and see him smash the little fairy. You grab your pockets full of candy and run for your life!" in output_lines[3]
    assert "You run as fast as you can and before you know it you are out of the forest. There are some lumberjacks about to go in and you fall to your knees and try to tell them there is an ogre, but you are making no sense." in output_lines[4]
    assert "You turn around nervously pointing at the forest." in output_lines[5]
    assert "“Ogre!” finally you manage the words as the ogre makes it out of the forest finally catching up." in output_lines[6]
    assert "The lumberjacks see him and launch an attack on the ogre leaving you on the ground with some candy still in your pockets." in output_lines[7]


def test_fairy_outcomes_two_return_statement():
    with patch("builtins.input", side_effect=["n"]):
        result = fairy_outcomes_win()
    assert result == "See you later!"


def test_man_opens_door():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            man_opens_door()
        output_lines = captured_output.getvalue().strip().split('\n')
    assert len(output_lines) == 14
    assert "He is putting on his jacket and seems surprised to see you standing there. Did he not hear you knocking?" in output_lines[0]
    assert "“Hey! who are you?” he asks" in output_lines[1]
    assert "“I am… I… my dad left me a while a go in the forest and now I am lost.”" in output_lines[2]
    assert "He looks around maybe looking to check that indeed you were alone. He looks down at you but you do not know what to make of it." in output_lines[3]
    assert "“I am leaving now, and I have nothing for you to steal so be on your way”" in output_lines[4]
    assert "You start crying." in output_lines[5]
    assert "“Look, I cannot jut let in some random kid from the forest, you could be a vampire for all I know. If you want water the well is over there. If you want to sleep you can sleep with the sheep but you better not kill them!”" in output_lines[6]
    assert "He hands you a handkerchief and moves past you." in output_lines[7]
    assert "“And do steal any of the candy either!”" in output_lines[8]
    assert "You make your way to the well, and get some water and then move towards the ship pen." in output_lines[9]
    assert "You pick a spot to fall a sleep on the hay." in output_lines[10]
    assert "All of a sudden you see some read eyes in front of you. VAMPIRE!" in output_lines[11]


def test_man_opens_door_return_statement():
    with patch("builtins.input", side_effect=["n"]):
        result = man_opens_door()
    assert result == "See you later!"


def test_voice_answers():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            voice_answers()
        output_lines = captured_output.getvalue().strip().split('\n')
    assert len(output_lines) == 11
    assert "You slowly enter the cabin" in output_lines[0]
    assert "You see an old lady by the kitchen stirring a pot" in output_lines[1]
    assert "“Who are you child, what do you want?”" in output_lines[2]
    assert "You explain your dad left you in the forest and never came back for you." in output_lines[3]
    assert "She looks at you and asks for your dads name." in output_lines[4]
    assert "“I know old Jack. Sit, you should have something to eat. We will go look for your dad after you eat”" in output_lines[5]
    assert "“I do not think my dad wants me back”. You say while having some soup." in output_lines[6]
    assert "“No, I do not imagine he does. You can stay here with me if you are willing to work and learn.”" in output_lines[7]
    assert "You slowly nod. And you live happily ever after." in output_lines[8]


def test_voice_answers_return_statement():
    with patch("builtins.input", side_effect=["n"]):
        result = voice_answers()
    assert result == "See you later!"


def test_no_answer_1():
    """test user input from no_answer() is captured"""
    with patch("builtins.input", side_effect=["1"]):
        result = no_answer()
    assert result == "You enter the house"


def test_no_answer_2():
    """test user input from no_answer() is captured"""
    with patch("game.no_answer", side_effect=["2"]):
        result = no_answer()
    assert result == garden_picking()


def test_no_answewr_path_other():
    """Asks the user for a choice when noone answers door - path not 1 or 2"""
    with patch("game.no_answer", side_effect=["4", "2"]):
        result = no_answer()
    assert result == garden_picking()


def test_go_into_cabin():
    """returns print statements from entering the cabin"""
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            go_into_cabin()
        output_lines = captured_output.getvalue().strip().split('\n')
    assert len(output_lines) == 5
    assert "You go into the house and see the cabin is empty." in output_lines[0]
    assert "The oven apears to be on." in output_lines[1]
    assert "You move towards it slowly and grab some bread for the table and mindlessly start eating it." in output_lines[2]
    assert "You slowly approach the oven to see what is cooking." in output_lines[3]
    assert "You hear some noise from behind you and before you know it… someone shoved you into the oven!" in output_lines[4]


def test_go_into_cabin_return_statement():
    result = go_into_cabin()
    assert result == "YOU WIN!"


def test_story_telling_print():
    lines = ['1', '2', '3']
    outcome = "win"
    with patch("builtins.print") as mock_print:
        story_telling(lines, outcome)
    for i, line in enumerate(lines):
        mock_print.assert_any_call(line)


def test_play_again_function_no():
    """test user input from play again, no"""
    with patch("game.play_again", side_effect=["n"]):
        result = play_again()
    assert result == "See you later!"


def test_play_again_yes():
    """test user input from play again, yes"""
    with patch("builtins.input", side_effect=["y"]):
        result = play_again()
    assert result == first_action()


def test_play_again_invalid_input():
    """test user input from invalid input, keeps asking"""
    with patch("game.play_again", side_effect=["4", "n"]):
        result = play_again()
    assert result == "See you later!"
'''