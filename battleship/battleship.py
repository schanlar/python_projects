"""
battleship.py
A simple Python approach to play the classic battleship game.
It supports two game modes:
    - Single mode      : one player against the computer
    - Two players mode : two players against each other
@author: Savvas Chanlaridis
@version: v2022-12-27
"""

import os
import random
from typing import *
from time import sleep


def main() -> None:
    # welcome()
    # game_mode = select_game_mode()
    pass
    return None

####
class ModeError(Exception):
    pass

def welcome() -> None:

    print("\t" + '#'*30)
    print('\t#' + ' '*28 + '#')
    print('\t#' + ' '*3 + "WELCOME TO BATTLESHIP!" + ' '*3 + '#')
    print('\t#' + ' '*28 + '#')
    print("\t" + '#'*30)
    print("The objective is to sink the ships of your opponent before they sink yours.".title())
    print("-"*3)
    return None

def goodbye() -> None:

    print("\t" + '#'*30)
    print('\t#' + ' '*28 + '#')
    print('\t#' + ' '*10 + "GOODBYE!" + ' '*10 + '#')
    print('\t#' + ' '*28 + '#')
    print("\t" + '#'*30)
    return None

def display_board() -> None:
    pass
    return None

def clear_monitor(delay_sec:Optional[int]=None) -> None:
    """
        Clears the terminal window
        delay_sec : int or None, delay clearing the terminal window
                    by that amount of seconds.
    """
    if delay_sec is None:
        if os.name == "nt": # For Windows
            os.system("cls")
        else: # For Linux/MacOS (name == "posix")
            os.system("clear")
    else:
        print("Clearing the monitor...")
        if os.name == "nt":
            sleep(delay_sec)
            os.system("cls")
        else:
            sleep(delay_sec)
            os.system("clear")
    return None

def select_game_mode() -> str:

    while True:
        answer:str = input("Input 1 for 1-player game or 2 for 2-player game: ")
        if answer.lower() == '1':
            return "single"
        elif answer.lower() == '2':
            return "double"
        else:
            print("I didn't understand that...")

def get_player_names(mode:str) -> Tuple[str, str]:

    print('-'*40)
    print("\t Game Mode: {}".format(mode.capitalize()))
    print('-'*40)
    if mode == "single":
        player_1:str = input("Name of player: ").capitalize()
        player_2:str = "Computer"
        clear_monitor()
        print("Good luck {}!".format(player_1))
        print('='*40)
        return (player_1, player_2)
    elif mode == "double":
        player_1 = input("Name of player 1: ").capitalize()
        player_2 = input("Name of player 2: ").capitalize()
        clear_monitor()
        print("Good luck {}, {}!".format(player_1, player_2))
        print('='*40)
        return (player_1, player_2)
    else:
        raise ModeError("game mode error")

def play_game(player_names:Tuple[str,str]) -> None:
    pass
    return None




if __name__ == "__main__":
    main()