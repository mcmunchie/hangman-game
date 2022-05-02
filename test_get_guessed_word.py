import hangman


def test_word_has_2_trailing_blanks():
    assert hangman.get_guessed_word(
        secret_word='jog', letters_guessed=['t', 'j', 'z']) == 'j_ _ '


def test_word_has_2_leading_blanks():
    assert hangman.get_guessed_word(
        secret_word='jog', letters_guessed=['r', 'd', 'g']) == '_ _ g'


def test_word_has_all_blanks():
    assert hangman.get_guessed_word(
        secret_word='jog', letters_guessed=['r', 'd', 'f']) == '_ _ _ '
