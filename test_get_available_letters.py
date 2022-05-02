import hangman

ALL_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def test_no_letters_guessed_returns_all_letters():
    assert hangman.get_available_letters(letters_guessed='') == ALL_LETTERS

def test_returns_letters_not_guessed():
    assert hangman.get_available_letters(letters_guessed='cl') == 'abdefghijkmnopqrstuvwxyz'

def test_all_letters_guessed_returns_empty_string():
    guessed = ALL_LETTERS
    assert hangman.get_available_letters(letters_guessed=guessed) == ''

def test_capitial_letters_guessed_returns_letters_not_guessed():
    assert hangman.get_available_letters(letters_guessed='AZ') == 'bcdefghijklmnopqrstuvwxy'
