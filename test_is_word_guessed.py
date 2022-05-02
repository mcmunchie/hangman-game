import hangman


def test_2_occurences_of_1_letter_in_word_returns_true():
    assert hangman.is_word_guessed(
        secret_word='happy', letters_guessed=['h', 'k', 'y', 'd', 'p', 'r', 'a']) is True


def test_2_occurences_of_2_letters_in_word_returns_true():
    assert hangman.is_word_guessed(
        secret_word='prosecutes', letters_guessed=['k', 'p', 'q', 'r', 'o', 'l', 's', 'e', 'c', 'u', 't']) is True


def test_3_occurences_of_1_letter_in_word_returns_true():
    assert hangman.is_word_guessed(
        secret_word='witticisms', letters_guessed=['j', 'w', 't', 'l', 'i', 'g', 'm', 's', 'c', 'r']) is True


def test_all_but_one_letter_guessed_returns_false():
    assert hangman.is_word_guessed(
        secret_word='wonderful', letters_guessed=['w', 'n', 'o', 'e', 't', 'd', 'f', 'r', 'l']) is False


def test_no_letters_guessed_returns_false():
    assert hangman.is_word_guessed(
        secret_word='car', letters_guessed=[]) is False


def test_2_letter_secret_word_returns_true():
    assert hangman.is_word_guessed(
        secret_word='ad', letters_guessed=['d', 'b', 'a']) is True


def test_2_letter_secret_word_returns_false():
    assert hangman.is_word_guessed(
        secret_word='ad', letters_guessed=['k', 'd']) is False
