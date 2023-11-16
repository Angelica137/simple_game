from game import intro

def test_intro(capsys):
	intro()
	captured = capsys.readouterr()
	assert captured.out.strip() == "You find yourself standing in an open field, filled with grass and yellow wildflowers. Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village..."