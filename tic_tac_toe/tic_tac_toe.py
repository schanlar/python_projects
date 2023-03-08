"""
tic_tac_toe.py

A simple Python approach to play the classic tic-tac-toe game.
It supports one game mode:
    - Double mode  : two players against each other
@author: Savvas Chanlaridis
@version: v2023-02-27
"""

import os
from typing import List, Tuple
from dataclasses import dataclass

NICKNAME_SIZE_MAX: int = 5

@dataclass 
class Player:
    nickname: str
    mark: str = ''
    status: int = -1
    score: int = 0
    row: int = -1 
    col: int = -1
    

def main() -> None:
    MAX_MOVES: int = 9
    keep_playing: bool = True
    answer: str = ''
    
    # Initialize
    print("Player 1: ")
    player1 = Player(get_nickname(NICKNAME_SIZE_MAX, "Player 1"))
    player1.mark = 'x'
    clear()
    print("Player 2: ")
    player2 = Player(get_nickname(NICKNAME_SIZE_MAX, "Player 2"))
    player2.mark = 'o'
    
    while(keep_playing):
        # (Re)-initialize board
        board: List[List[str]] = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        moves: int = 0 # Keep track of moves played
        player1.status = player2.status = -1 # Reset status
        
        while (moves < MAX_MOVES):
            if (moves == 0):
                clear()
                display_board(board)
            
            player1.row, player1.col = get_move(board, player1)
            board[player1.row][player1.col] = player1.mark
            moves += 1
            clear()
            display_board(board)
                
            if (moves >= 5): # needs minimum of 5 moves before someone wins
                if (check_board(board, player1)):
                    player1.score += 1 
                    player1.status = 1 
                    player2.status = 0 
                    break
                elif (check_board(board, player2)):
                    player2.score += 1 
                    player2.status = 1 
                    player1.status = 0 
                    break
            
            if (moves == MAX_MOVES): break
            player2.row, player2.col = get_move(board, player2)
            board[player2.row][player2.col] = player2.mark
            moves += 1
            clear()
            display_board(board)
            
            if (moves >= 5): # needs minimum of 5 moves before someone wins
                if (check_board(board, player1)):
                    player1.score += 1 
                    player1.status = 1 
                    player2.status = 0 
                    break
                elif (check_board(board, player2)):
                    player2.score += 1 
                    player2.status = 1 
                    player1.status = 0 
                    break
        
        if (player1.status == player2.status):
            print("It's a draw!")
        elif (player1.status > player2.status):
            print("%s WINS!" % player1.nickname)
        else:
            print("%s WINS!" % player2.nickname)
            
        while True:
            answer = input("Do you want to play again? [y/n] ")
            if (answer.lower() == 'n'):
                keep_playing = False
                print("Final score:\n---------")
                print("%s: %i pts" % (player1.nickname, player1.score))
                print("%s: %i pts" % (player2.nickname, player2.score))
                break
            elif (answer.lower() == 'y'):
                clear()
                break
            else:
                print("ERROR: invalid answer!")
            
    return None
    
def get_move(board: List[List[str]], player: Player) -> Tuple[int, int]:
    while (True):
        s: str = input("%s, it's your turn! Please give coordinates (e.g. 12): " % player.nickname)
        
        if (len(s) > 2):
            print("ERROR: too many arguments")
            continue
        elif (len(s) < 2):
            print("ERROR: too few arguments")
            continue

        if not s.isdigit():
            print("ERROR: coordinates must be two number in [0,2]!")
            continue
        
        if (int(s[0]) < 0 or int(s[0]) > 2):
            print("ERROR: %i is out of bounds!" % int(s[0]))
            continue
        
        if (int(s[1]) < 0 or int(s[1]) > 2):
            print("ERROR: %i is out of bounds!" % int(s[1]))
            continue
            
        if not board[int(s[0])][int(s[1])].isspace():
            print("ERROR: position is already occupied!")
            continue
            
        return int(s[0]), int(s[1])

def check_board(board: List[List[str]], player: Player) -> bool:
    # Check rows for winner
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == player.mark):
            return True
            
    # Check rows for winner
    for j in range(3):
        if (board[0][j] == board[1][j] == board[2][j] == player.mark):
            return True
    
    # Check diagonals for winners
    if (board[0][0] == board[1][1] == board[2][2] == player.mark):
        return True
    elif (board[2][0] == board[1][1] == board[0][2] == player.mark):
        return True
    
    return False

def display_board(board: List[List[str]]) -> None:
    print("\t0\t1\t2\t\n")
    print("0\t%s   |\t%s   |\t%s\t" % (board[0][0], board[0][1], board[0][2]))
    print(" "*5 + "-"*23)
    print("1\t%s   |\t%s   |\t%s\t" % (board[1][0], board[1][1], board[1][2]))
    print(" "*5 + "-"*23)
    print("2\t%s   |\t%s   |\t%s\t" % (board[2][0], board[2][1], board[2][2]))
    return None
    
def get_nickname(size: int, default: str) -> str:
    while (True):
        nickname = input("Enter a nickname up to %i characters long: " % size)
        if (len(nickname) > size):
            print("Nickname cannot be longer than %i characters" % size)
        elif (len(nickname) == 0 or nickname.isspace()):
            return default
        else:
            return nickname
            
def clear() -> None:
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Linux/MacOS (name == "posix")
        os.system("clear")
    return None


if (__name__ == "__main__"):
    main()