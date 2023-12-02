from src.actions.play_game import *
from unittest.mock import patch


def test_play_game(capsys):
    play_game()
    captured = capsys.readouterr()
    assert "Hi, " in captured.out
    assert "You are in the middle of an enchanted forest" in captured.out