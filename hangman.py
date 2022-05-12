import random
from typing import Counter

# global constants
WORDLIST_FILENAME = "words.txt"
ALL_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
VOWELS = 'aeiou'
MAX_GUESSES = 6
MAX_WARNINGS = 3


def load_words():
    '''
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
    '''
    print("\nLoading word list from file...")
    word_file = open(WORDLIST_FILENAME, 'r')
    line = word_file.readline()
    word_file.close()

    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return tuple(wordlist)


def choose_word(wordlist):
    '''
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    '''
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing;
      assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Define variables
    counter = 0
    # Iterate over each letter in secret_word
    for letter in secret_word:
        # Determine if letter has been guessed by checking if its in letters_guessed
        if letter in letters_guessed:
            # If letter in letters_guessed, counter increase by 1
            counter += 1
    # After all letters checked, compare counter to number of letters in secret_word
    # If count the same, return True
    if counter == len(secret_word):
        return True
    # Otherwise, return False
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # Assign guessed_word to empty string
    guessed_word = ""
    # Iterate over each letter in secret_word
    for letter in secret_word:
        # If letter is guessed, append letter to guessed_word
        if letter in letters_guessed:
            guessed_word += letter
        # If letter is not guessed, append '_ ' to guessed_word
        else:
            guessed_word += '_ '
    # Return guessed_word
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_guessed = letters_guessed.lower()

    avail_letters = ''
    for letter in ALL_LETTERS:
        if letter not in letters_guessed:
            avail_letters += letter
    return avail_letters


def invalid_guess(warnings_remaining, guesses_remaining):
    '''
    Call this function when the user enters a letter already guessed or
    a symbol that is not a letter.

    The function supports the following game rules:
      1. If the user has one or more warning left, the user should lose one warning.
      2. If the user has no remaining warnings, they should lose one guess.

    This function returns new values for warnings and guesses remaining.
    warnings_remaining: int, the warnings remainin before the invalid guess
    guesses_remaining: int, the guesses remaining before the invalid guess
    returns: int, int, the number of warnings and guesses remaining after the invalid guess
    '''
    if warnings_remaining > 0:
        warnings_remaining -= 1
    else:
        if guesses_remaining > 0:
            guesses_remaining -= 1
    return warnings_remaining, guesses_remaining


def incorrect_guess(guessed_letter, guesses_remaining):
    '''
    Call this function when the user makes a guess that is valid, but it doesn't
    match a letter in the secret word.

    The function supports the following game rules:
      3. Consonants: if user inputs a consonant that hasn't been guessed and the consonant is not in the secret word, the user loses one guess.
      4. Vowels: if the vowel hasn't been guessed and the vowel is not in the secret word, the user loses two guesses.

    This function returns a new value for the number of guesses remaining.
    guessed_letter: string, the letter guessed by the player
    guesses_remaining: int, the guesses remaining before the incorrect guess
    returns: int, the number of guesses remaining after incorrect bad guess
    '''
    if guessed_letter in VOWELS:
        if guesses_remaining > 1:
            guesses_remaining -= 2
        else:
            guesses_remaining = 0
    else:
        if guesses_remaining > 0:
            guesses_remaining -= 1
    return guesses_remaining


def calculate_score(guesses_remaining, secret_word):
    '''
    Call this function to calculate the user's score at the end of the game.

    guesses_remaining: int, guesses remaining at the conclusion of the game
    secret_word, string, the secret word
    returns: int, the score if guesses_remaining is > 0; otherwise, 0.
    '''
    temp_word = ''
    score = 0
    for ch in secret_word:  # ch means character
        if ch not in temp_word:
            temp_word += ch  # would iterate once for each ch (no repeat letters)
        # Calculated score is number of guesses_remaining * the number of
        # unique letters in secret_word
    score = guesses_remaining * len(temp_word)
    # Return score if guesses_remaining > 0
    if guesses_remaining > 0:
        return score
    # Else, return 0
    else:
        return 0


def prompt_for_letter(guesses_remaining, warnings_remaining, available_letters):
    '''
    Prompt the user to enter an available letter. Converts the letter to lowercase
    before returning it.

    guesses_remaining: int, guesses remaining
    warnings_remaining, int, warnings remaining
    available_letters, string, available letters for the user to choose from.
    returns: string, lowercased letter input by the user
    '''
    # Display guesses_remaining, warnings_remaining, and available_letters
    print('You have', int(guesses_remaining), 'guesses left.\n' 'You have', int(
        warnings_remaining), 'warnings left.', '\nAvailable letters:', str(available_letters))
    # Prompt user to enter available letter, convert letter to lowercase before
    # returning it
    letter_guess = str(input('Enter a letter: '))
    # Return lowercase letter
    return letter_guess.lower()


def display_game_outcome(score, secret_word):
    '''
    Displays the outcome of the game.
    If the score is greater than 0, display 'Congratulations, you won!'
    and the user's score. Otherwise, display 'Sorry, you ran out of guesses' and
    the secret word.

    score, int, the user's score
    secret_word, string, the secret word
    '''
    # If score is greater than 0, display first message
    if score > 0:
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)

    # Else, display other message
    else:
        print("Sorry, you ran out of guesses.")
        print("The word was", secret_word)


def main():
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the secret word.

    * After each guess, you should display to the user the
      partially guessed word so far.
    '''
    # load the words into a list
    wordlist = load_words()

    guesses_remaining = MAX_GUESSES
    warnings_remaining = MAX_WARNINGS

    # choose a word from the word list
    secret_word = choose_word(wordlist)

    # used to keep track of letters guessed
    letters_guessed = ''

    # available letters (not yet guessed) for the player to choose from
    available_letters = get_available_letters(letters_guessed)

    # The guessed_word contains '_ ' for each letter not guessed.
    # Initially, none of the letters will be guessed, so the guessed_word
    # will contain '_' for every character after the following line
    # executes.
    guessed_word = get_guessed_word(secret_word, letters_guessed)

    print("\nLet's play:", guessed_word)

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):

        # Print game begin and ask user for letter
        letter = prompt_for_letter(
            guesses_remaining, warnings_remaining, available_letters)
        if letter not in ALL_LETTERS:
            warnings_remaining, guesses_remaining = invalid_guess(
                warnings_remaining, guesses_remaining)
            print('That is not a valid letter.')
            print('-------------------')
        elif letter in letters_guessed:
            warnings_remaining, guesses_remaining = invalid_guess(
                warnings_remaining, guesses_remaining)
            print("Sorry, that letter has already been guessed.")
            print('-------------------')

        elif letter in secret_word:
            letters_guessed += letter
            available_letters = get_available_letters(letters_guessed)
            print("Good guess:", get_guessed_word(
                secret_word, letters_guessed))
            print('-------------------')

        elif letter not in secret_word:
            letters_guessed += letter
            available_letters = get_available_letters(letters_guessed)
            guesses_remaining = incorrect_guess(letter, guesses_remaining)
            print("Sorry, that letter is not in my word:",
                  get_guessed_word(secret_word, letters_guessed))
            print('-------------------')

    score = calculate_score(guesses_remaining, secret_word)
    display_game_outcome(score, secret_word)
    print()
    
if __name__ == "__main__":
    main()
