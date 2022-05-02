import hangman


def test_warnings_remaining_decremented():
    warnings, guesses = hangman.invalid_guess(2, 6)
    assert warnings == 1
    assert guesses == 6


def test_guesses_remaining_decremented():
    warnings, guesses = hangman.invalid_guess(0, 6)
    assert warnings == 0
    assert guesses == 5


def test_guesses_remaining_when_warnings_is_negative():
    warnings, guesses = hangman.invalid_guess(-1, 1)
    assert warnings == -1
    assert guesses == 0


def test_guesses_and_warnings_remaining_not_decremented_when_0():
    warnings, guesses = hangman.invalid_guess(0, 0)
    assert warnings == 0
    assert guesses == 0


def test_warnings_remaining_not_decremented_when_negative():
    warnings, guesses = hangman.invalid_guess(-1, 0)
    assert warnings == -1
    assert guesses == 0


def test_guesses_remaining_not_decremented_when_negative():
    warnings, guesses = hangman.invalid_guess(0, -1)
    assert warnings == 0
    assert guesses == -1
