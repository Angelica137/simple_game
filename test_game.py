from game import *

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


def test_second_action(monkeypatch, capfd):
    monkeypatch.setattr('game.get_user_input', lambda _: 'second')
    result = get_user_input("Q: ")
    with capfd.disabled():
        result = second_action()
        
    assert result == 'second'