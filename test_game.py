import time
from game import *
from freezegun import freeze_time

def test_get_user_input(monkeypatch):
    monkeypatch.setattr('game.get_user_input', lambda _: 'test_input')
    result = get_user_input("Q: ")
    assert result == 'test_input'

def test_intro(monkeypatch, capfd):
    monkeypatch.setattr('game.get_user_input', lambda _: 'test_input')

    # Redirect stdout to capfd
    with capfd.disabled():
        result = intro()

    assert result == 'test_input'

def test_get_user_input_2(monkeypatch):
    monkeypatch.setattr('game.get_user_input', lambda _: 'second')
    result = get_user_input("Second: ")
    assert result == 'second'

def test_second_action(monkeypatch, capfd):
    monkeypatch.setattr('game.get_user_input', lambda _: 'second')
    with capfd.disabled():
        result = second_action()
        
    assert result == 'second'
    

def test_pause():
    with freeze_time("2022-01-01 00:00:00"):
        start_time = time.time()
        result = pause()
        end_time = time.time()
        
    assert result == "expected_result"
    assert end_time - start_time >= 5