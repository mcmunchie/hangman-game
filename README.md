# Hangman Game

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Table of Contents
+ [Purpose](https://github.com/mcmunchie/hangman-game#purpose)
+ [Basic Hangman](https://github.com/mcmunchie/hangman-game#basic-hangman)
+ [Game Rules & Requirements](https://github.com/mcmunchie/hangman-game#game-rules--requirements)
+ [Example Output](https://github.com/mcmunchie/hangman-game#example-output)

## Purpose
To learn how to create functions in Python and practice looping mechanisms for repeating computational processes.

## _Basic Hangman_
This Python program is a version of the classic word game Hangman. More information about the game can be found [here][wiki].

[wiki]: <https://en.wikipedia.org/wiki/Hangman_(game)>

## Game Rules & Requirements
1. User starts with 3 warnings
2. If user inputs anything besides an alphabet (symbols, numbers), tell user that they can only input an alphabet 
    + If user has one or more warning left, the user should lose one warning. Tell user the number of remaining warnings
    + If user has no remaining warnings, they should lose one guess
3. If user inputs a letter that has already been guessed, print a message telling the user the letter has already been guessed before
    + If user has one or more warning left, the user should lose one warning. Tell user the number of remaining warnings
    + If user has no warnings, they should lose one guess
4. If user inputs a letter that hasn’t been guessed before and the letter is in the secret word, user loses ***no** guesses
5. **Consonants:** If user inputs a consonant that hasn’t been guessed and the consonant is not in the secret word, user loses **one** guess if it’s a consonant
6. **Vowels:** If vowel hasn’t been guessed and the vowel is not in the secret word, user loses **two** guesses. Vowels are _a, e, i, o,_ and _u. y_ does not count as a vowel
    
    _Example Game Implementation:_
    ``` 
    Let's play: _ _ _ _ _ _ _ _ _ _ 
    You have 6 guesses left.
    You have 3 warnings left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Enter a letter: t
    Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ _ 
    --------------------
    You have 5 guesses left.
    You have 3 warnings left.
    Available letters: abcdefghijklmnopqrsuvwxyz
    Enter a letter:
    ```

## Example Output
> Lose game
<img src=img\lose-hangman.png />

> Win game (part one)
<img src=img\win-hangman-1.png />

> Win game (part two)
<img src=img\win-hangman-2.png />

> Unit tests
<img src=img\test-hangman.png />
