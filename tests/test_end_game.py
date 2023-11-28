from src.end_game import *
from unittest.mock import patch


def test_play_again_function_no():
    """test user input from play again, no"""
    with patch("src.end_game.play_again", side_effect=["n"]):
        result = play_again()
    assert result == "See you later!"


def test_play_again_yes(): # this test fails I think it cannot run here because of the order
    """test user input from play again, yes"""
    with patch("src.end_game.play_again", side_effect=["y"]):
        result = play_again()
    assert result == first_action()


def test_play_again_invalid_input():
    """test user input from invalid input, keeps asking"""
    with patch("src.end_game.play_again", side_effect=["4", "n"]):
        result = play_again()
    assert result == "See you later!"