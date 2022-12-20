"""
hangman.py

A simple Python approach to play the classic hangman game.
It supports two game modes:
    - Single mode      : one player against the computer
    - Two players mode : two players against each other

@author: Savvas Chanlaridis
@version: v2022-12-19
"""

import os
import random
from typing import *
import pathlib
from time import sleep


def main() -> None:
    # Step 0.0: Load dictionary of valid words
    words = load_words()

    while True:

        # Step 0.1: Greetings and selection of game mode (single or double)
        welcome()
        game_mode = select_game_mode()

        # Step 1: Determine the hidden work
        word_exists = False
        number_of_tries = 1
        while not word_exists:
            word = get_word(game_mode, words, _tries=number_of_tries)
            number_of_tries += 1
            word_exists = check_word(word, words)

        # Step 2: Play the game
        if game_mode == "double": clear_monitor()
        play_game(word, player_names=player_names(game_mode))

        # Step 3: Ask if they want to play again
        play_again:str = input("Do you want to play again? (y/n) ")
        if play_again.lower() == 'y':
            clear_monitor(False)
        elif play_again.lower() == 'n':
            goodbye()
            return None
        else:
            print("I didn't understand that! I am exiting the game...")
            goodbye()
            return None



class ModeError(Exception):
    pass

def display_hanger(body_parts:Dict[str, str]) -> None:

    print("\t\t+-----+")
    print("\t\t|     {head}".format(**body_parts))
    print("\t\t|   {left_arm}{torso}{right_arm}".format(**body_parts))
    print("\t\t|    {left_leg} {right_leg}".format(**body_parts))
    print("\t\t|")
    return None

def display_hidden_word(hidden_word:str) -> None:
    print("The word is: {} ({} letters)".format(hidden_word, len(hidden_word)))
    return None

def clear_monitor(delay:bool=True) -> None:
    """Clears the terminal window"""
    if delay:
        print("Clearing...")
        if os.name == "nt": # For Windows
            sleep(2)
            os.system("cls")
        else: # For Linux/MacOS (name == "posix")
            sleep(2)
            os.system("clear")
    else:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    return None

def load_words(file:Union[str, pathlib.Path]="words.txt") -> List[str]:

    words:List[str] = []
    with open(file) as f:
        for line in f:
            line_words = line.strip().split('-')
            for word in line_words:
                if len(word) >=3 :
                    words.append(word.upper())
    return words

def get_lengths(dict_:Sequence[str]) -> Tuple[int, int]:

    current_min:int = 10_000
    current_max:int = 0
    for word in dict_:
        if len(word) > current_max : current_max = len(word)
        if len(word) < current_min : current_min = len(word)
    return (current_min, current_max)

def select_game_mode() -> str:

    while True:
        answer:str = input("Type 's/S' or 'd/D' for single or double mode respectively: ")
        if answer.lower() == 'd':
            return "double"
        elif answer.lower() == 's':
            return "single"
        else:
            print("I didn't understand that...")

def get_word(mode:str, 
            dict_:Sequence[str], 
            length:int=0,
            _tries:int=1) -> str:

    if mode == "double":
        if _tries == 1:
            return input("Provide the word: ").upper()
        else:
            print("The world is not valid!")
            return input("Provide a new word: ").upper()
    elif mode == "single":
        while True:
            try:
                length = int(input("Type '0' for word of random length, else give length of random word (between {} and {}): ".format(*get_lengths(dict_))))
                # assert length in range(*get_lengths(dict_))
                valid_lengths:List[int] = [i for i in range(get_lengths(dict_)[0], get_lengths(dict_)[1]+1)]
                valid_lengths.append(0)
                if length not in valid_lengths:
                    raise ValueError

                if length == 0:
                    return random.choice(dict_)
                else:
                    candidate_words:List[str] = []
                    for word in dict_:
                        if len(word) == length:
                            candidate_words.append(word)
                    return random.choice(candidate_words)
            except ValueError:
                print("length must be an integer between {} and {}".format(*get_lengths(dict_)))
            # except AssertionError:
            #     print("length must be between {} and {}".format(*get_lengths(dict_)))
    else:
        raise ModeError("game mode error")

def check_word(word:str, dict_:Sequence[str]) -> bool:
    """
    Checks if the given word is valid.
    A valid word is a word that exists in
    a user provided sequence of valid words.
    """
    if word in dict_:
        return True
    else:
        return False

def player_names(mode:str) -> Tuple[str, str]:

    print('-'*40)
    print("\t Game Mode: {}".format(mode.capitalize()))
    print('-'*40)
    if mode == "single":
        player_1:str = input("Name of player: ").capitalize()
        player_2:str = "Computer"
        clear_monitor(False)
        print("Good luck {}!".format(player_1))
        print('='*40)
        return (player_1, player_2)
    elif mode == "double":
        player_1 = input("Name of player 1 (word seeker): ").capitalize()
        player_2 = input("Name of player 2 (word provider): ").capitalize()
        clear_monitor(False)
        print("Good luck {}, {}!".format(player_1, player_2))
        print('='*40)
        return (player_1, player_2)
    else:
        raise ModeError("game mode error")

def display_tries_left(tries:int, max_tries:int=6) -> None:

    print("{} tries left".format(max_tries - tries))
    return None

def display_used_letters(letters:List[str]) -> None:

    print("Chosen letters:", letters)
    return None

def get_new_letter(chosen_letters:List[str]) -> str:
    # Check if letter has been used before
    letter_is_valid:bool = False
    while not letter_is_valid:
        letter:str = input("Guess letter: ").upper()
        if not letter.isalpha():
            print("All letters must be alphabets!")
        elif len(letter) > 1:
            print("Letter must be a single character!")
        elif letter in chosen_letters:
            print("You've chosen this letter already!")
        else:
            letter_is_valid = True
    return letter

def play_game(word:str,
            player_names:Tuple[str,str],
            max_tries:int=6) -> None:

    # Put characters of word into a list
    word_characters:List[str] = [char for char in word]
    hidden_word_characters:List[str] = ['-' for _ in word]
    # Initialize hidden word
    hidden_word:str = '-'*len(word)
    # Used for updating hanger function
    body_parts:Dict[str, str] = dict(head='', torso='', left_arm='  ', right_arm='  ', left_leg='', right_leg='')
    # Used for showing played letters
    chosen_letters:List[str] = [] 
    # Number of tries
    tries:int = 0
    
    while (hidden_word.count('-') > 0) and (tries < max_tries):
        display_hanger(body_parts)
        display_tries_left(tries)
        display_hidden_word(hidden_word)
        display_used_letters(chosen_letters)

        letter = get_new_letter(chosen_letters)
        chosen_letters.append(letter)
        clear_monitor(False)

        if letter in word:
            for idx, char in enumerate(word_characters):
                if char == letter:
                    hidden_word_characters[idx] = char
            # Re-initialize hidden word        
            hidden_word = ''
            for element in hidden_word_characters: hidden_word = hidden_word + element
        else:
            tries += 1
            if tries == 1:
                body_parts.update({"head":'o'})
            elif tries == 2:
                body_parts.update({"torso":'+'})
            elif tries == 3:
                body_parts.update({"left_arm":"--"})
            elif tries == 4:
                body_parts.update({"right_arm":"--"})
            elif tries == 5:
                body_parts.update({"left_leg":'/'})
            else:
                body_parts.update({"right_leg":"\\"})
    
    if tries >= max_tries:
        display_hanger(body_parts)
        print("{} wins! The word was \"{}\"".format(player_names[1].capitalize(), word))
    elif hidden_word.count('-') == 0:
        display_hanger(body_parts)
        print("{} wins! The word was \"{}\"".format(player_names[0].capitalize(), word))
    return None

def goodbye() -> None:

    print("\t" + '#'*30)
    print('\t#' + ' '*28 + '#')
    print('\t#' + ' '*10 + "GOODBYE!" + ' '*10 + '#')
    print('\t#' + ' '*28 + '#')
    print("\t" + '#'*30)
    return None

def welcome() -> None:

    print("\t" + '#'*30)
    print('\t#' + ' '*28 + '#')
    print('\t#' + ' '*5 + "WELCOME TO HANGMAN" + ' '*5 + '#')
    print('\t#' + ' '*28 + '#')
    print("\t" + '#'*30)
    return None



if __name__ == "__main__":
    main()