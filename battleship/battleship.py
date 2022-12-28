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

MAX_NAME:int = 18 # maximum number of characters allowed for a name
POSITIONS:Dict[str, str] = dict(
    p1a1 = ' ', p1a2 = ' ', p1a3 = ' ', p1a4 = ' ', p1a5 = ' ',
    p1b1 = ' ', p1b2 = ' ', p1b3 = ' ', p1b4 = ' ', p1b5 = ' ',
    p1c1 = ' ', p1c2 = ' ', p1c3 = ' ', p1c4 = ' ', p1c5 = ' ',
    p1d1 = ' ', p1d2 = ' ', p1d3 = ' ', p1d4 = ' ', p1d5 = ' ',
    p1e1 = ' ', p1e2 = ' ', p1e3 = ' ', p1e4 = ' ', p1e5 = ' ',
    p2a1 = ' ', p2a2 = ' ', p2a3 = ' ', p2a4 = ' ', p2a5 = ' ',
    p2b1 = ' ', p2b2 = ' ', p2b3 = ' ', p2b4 = ' ', p2b5 = ' ',
    p2c1 = ' ', p2c2 = ' ', p2c3 = ' ', p2c4 = ' ', p2c5 = ' ',
    p2d1 = ' ', p2d2 = ' ', p2d3 = ' ', p2d4 = ' ', p2d5 = ' ',
    p2e1 = ' ', p2e2 = ' ', p2e3 = ' ', p2e4 = ' ', p2e5 = ' '
)

def main() -> None:
    welcome()
    game_mode = select_game_mode()
    names = get_player_names(game_mode)
    display_board(POSITIONS, names)
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

def display_board(positions:Dict[str, str], player_names:Tuple[str,str]) -> None:
    print("    1    2    3    4    5\t\t\t    1    2    3    4    5")
    print('  ' + '-'*26 + "\t\t\t" + '  ' + '-'*26)
    print("a | {p1a1}  | {p1a2}  | {p1a3}  | {p1a4}  | {p1a5}  |\t\t\ta | {p2a1}  | {p2a2}  | {p2a3}  | {p2a4}  | {p2a5}  |".format(**positions))
    print('  ' + '-'*26 + "\t\t\t" + '  ' + '-'*26)
    print("b | {p1b1}  | {p1b2}  | {p1b3}  | {p1b4}  | {p1b5}  |\t\t\tb | {p2b1}  | {p2b2}  | {p2b3}  | {p2b4}  | {p2b5}  |".format(**positions))
    print('  ' + '-'*26 + "\t\t\t" + '  ' + '-'*26)
    print("c | {p1c1}  | {p1c2}  | {p1c3}  | {p1c4}  | {p1c5}  |\t\t\tc | {p2c1}  | {p2c2}  | {p2c3}  | {p2c4}  | {p2c5}  |".format(**positions))
    print('  ' + '-'*26 + "\t\t\t" + '  ' + '-'*26)
    print("d | {p1d1}  | {p1d2}  | {p1d3}  | {p1d4}  | {p1d5}  |\t\t\td | {p2d1}  | {p2d2}  | {p2d3}  | {p2d4}  | {p2d5}  |".format(**positions))
    print('  ' + '-'*26 + "\t\t\t" + '  ' + '-'*26)
    print("e | {p1e1}  | {p1e2}  | {p1e3}  | {p1e4}  | {p1e5}  |\t\t\te | {p2e1}  | {p2e2}  | {p2e3}  | {p2e4}  | {p2e5}  |".format(**positions))
    print('  ' + '-'*26 + "\t\t\t" + '  ' + '-'*26)
    print("  Player: {}\t\t\t  Player: {}".format(player_names[0].ljust(MAX_NAME), player_names[1]))
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
        while True:
            player_1:str = input("Name of player: ").capitalize()
            if len(player_1) > MAX_NAME:
                print("Player's name cannot exceed {} characters! Please try again.".format(MAX_NAME))
            else: break
        player_2:str = "Computer"
        clear_monitor()
        print("Good luck {}!".format(player_1))
        print('='*50)
        return (player_1, player_2)
    elif mode == "double":
        while True:
            player_1 = input("Name of player 1: ").capitalize()
            if len(player_1) > MAX_NAME:
                print("Player's name cannot exceed {} characters! Please try again.".format(MAX_NAME)) 
            else: break
        while True:
            player_2 = input("Name of player 2: ").capitalize()
            if len(player_2) > MAX_NAME:
                print("Player's name cannot exceed {} characters! Please try again.".format(MAX_NAME))
            else: break
        clear_monitor()
        print("Good luck {}, {}!".format(player_1, player_2))
        print('='*50)
        return (player_1, player_2)
    else:
        raise ModeError("game mode error")

def play_game(player_names:Tuple[str,str]) -> None:
    pass
    return None




if __name__ == "__main__":
    main()