from src.actions.knock_knock import *
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch



def test_forest_cabin_path_1_knock_on_door():
    """Asks the user for a choice at the cabin - path knock on door.
        Do not play again."""
    with patch("src.actions.part_one.first_action", return_value='1'), \
    patch('random.choice', return_value='A young man opens the door.'):
        result = forest_cabin()
    assert result == "GAME OVER."


def test_forest_cabin_path_2_go_to_garden():
    """Asks the user for a choice at the cabin - path go to garden"""
    with patch("src.actions.part_one.forest_cabin", side_effect=["2"]):
        result = forest_cabin()
    assert result == garden_picking()

'''
def test_forest_cabin_path_other():
    """Asks the user for a choice at the cabin - path not 1 or 2"""
    with patch("src.part_one.first_action", side_effect=["4", "2"]):
        result = forest_cabin()
    assert result == garden_picking()



def test_cabin_knock(monkeypatch):
    """Retunrs a value from the list - outcome lose, choose no"""
    monkeypatch.setattr(random, 'choice', lambda seq: seq[0])
    result = cabin_knock()
    assert result == "See you later!"


def test_man_opens_door():
    """User does not want to play, enter n."""
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
    """User does not want to play, enter n"""
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
    with patch("src.knock_knock.no_answer", side_effect=["2"]):
        result = no_answer()
    assert result == garden_picking()


def test_no_answewr_path_other():
    """Asks the user for a choice when noone answers door - path not 1 or 2"""
    with patch("src.knock_knock.no_answer", side_effect=["4", "2"]):
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
'''