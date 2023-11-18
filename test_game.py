from game import *
from freezegun import freeze_time
from io import StringIO
from contextlib import redirect_stdout

def test_get_user_input(monkeypatch):
    monkeypatch.setattr('game.get_user_input', lambda _: 'Ana')
    result = get_user_input("Welcome, player 1. What is your name?\n")
    assert result == 'Ana'


def test_intro(monkeypatch, capfd):
    monkeypatch.setattr('game.get_user_input', lambda _: 'Ana')
    # Redirect stdout to capfd
    with capfd.disabled():
        result = intro()
    assert result == 'Welcome, Ana'


def test_pause():
    with freeze_time("2022-01-01 00:00:00"):
        result = pause()       
    assert result == time.sleep(2)
    

def test_long_story():
    with StringIO() as captured_output:
        with redirect_stdout(captured_output):
            long_story()           
        output_lines = captured_output.getvalue().strip().split('\n')
        
    assert len(output_lines) == 3
    assert "You are in the middle of an enchanted forest where your parents left you with some bread" in output_lines[0]
    assert "After walking for a while you come across a cabin made of ginger bread and candy." in output_lines[1]
    assert "You are suspicious, but you are also tired and hungry." in output_lines[2]


def test_first_action(monkeypatch, capfd):
    monkeypatch.setattr('game.get_user_input', lambda _: 1)
    with capfd.disabled():
        result = first_action()        
    assert result == 1
    

def test_knock_knock():
    result = first_action()
    if result == '1':
        assert knock_knock() == "A young man opens the door."
    if result == '2':
        assert knock_knock() == "You go into stealth mode and move around the property towards the neares candy bush."
    else:
        assert knock_knock() == first_action()

