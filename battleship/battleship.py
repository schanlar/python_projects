"""
battleship.py
An OOP Python approach to play the classic battleship game.
It supports two game modes:
    - Single mode      : one player against the computer
    - Two players mode : two players against each other
@author: Savvas Chanlaridis
@version: v2023-01-10
"""

import os
import random
from dataclasses import dataclass
from time import sleep
from termcolor import colored

try:
    from typing import List, Tuple, Dict, Set, Type, NewType, Optional
except ImportError:
    os.system("pip install typing")
    from typing import List, Tuple, Dict, Set, Type, NewType, Optional

# GameConfig = NewType("GameConfig", type)


class Messages:
    @staticmethod
    def info(text: str) -> None:
        print(colored(text, "green"))
        return None

    @staticmethod
    def warning(text: str) -> None:
        print(colored(f"Warning:\n{text}", "yellow"))
        return None

    @staticmethod
    def error(text: str) -> None:
        print(colored(f"Error:\n{text}", "red"))
        return None


class Greetings:
    @staticmethod
    def welcome() -> None:
        """
            It prints out a welcome message.
        """
        print("\n")
        print("\t\t\t" + "#" * 30)
        print("\t\t\t#" + " " * 28 + "#")
        print(
            "\t\t\t#"
            + " " * 3
            + colored("WELCOME TO BATTLESHIP!", "cyan")
            + " " * 3
            + "#"
        )
        print("\t\t\t#" + " " * 28 + "#")
        print("\t\t\t" + "#" * 30)
        print("\n")
        print(
            "The objective is to sink the ships of your opponent before they sink yours.".title()
        )
        print("\t\t\t\t" + "-" * 5)
        return None

    @staticmethod
    def goodbye() -> None:
        """
            It prints out a farewell mesage.
        """
        print("\n")
        print("\t\t\t" + "#" * 30)
        print("\t\t\t#" + " " * 28 + "#")
        print("\t\t\t#" + " " * 10 + colored("GOODBYE!", "cyan") + " " * 10 + "#")
        print("\t\t\t#" + " " * 28 + "#")
        print("\t\t\t" + "#" * 30)
        return None


class Display:
    @staticmethod
    def clear_monitor(delay_sec: Optional[int] = None) -> None:
        """
            Clears the terminal window.

            ARGS
            ==========
                delay_sec : int or None, delay clearing the terminal window by that amount of seconds.
            
            RETURNS
            ==========
                None.
        """
        if delay_sec is None:
            if os.name == "nt":  # For Windows
                os.system("cls")
            else:  # For Linux/MacOS (name == "posix")
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

    @staticmethod
    def board(
        p1_positions: Dict[str, str],
        p2_positions: Dict[str, str],
        player_names: Tuple[str, str],
    ) -> None:
        """Displays the board"""
        print("    1    2    3    4    5\t\t\t    1    2    3    4    5")
        print("  " + "-" * 26 + "\t\t\t" + "  " + "-" * 26)
        print(
            "a | {p1a1}  | {p1a2}  | {p1a3}  | {p1a4}  | {p1a5}  |\t\t\ta | {p2a1}  | {p2a2}  | {p2a3}  | {p2a4}  | {p2a5}  |".format(
                **p1_positions, **p2_positions
            )
        )
        print("  " + "-" * 26 + "\t\t\t" + "  " + "-" * 26)
        print(
            "b | {p1b1}  | {p1b2}  | {p1b3}  | {p1b4}  | {p1b5}  |\t\t\tb | {p2b1}  | {p2b2}  | {p2b3}  | {p2b4}  | {p2b5}  |".format(
                **p1_positions, **p2_positions
            )
        )
        print("  " + "-" * 26 + "\t\t\t" + "  " + "-" * 26)
        print(
            "c | {p1c1}  | {p1c2}  | {p1c3}  | {p1c4}  | {p1c5}  |\t\t\tc | {p2c1}  | {p2c2}  | {p2c3}  | {p2c4}  | {p2c5}  |".format(
                **p1_positions, **p2_positions
            )
        )
        print("  " + "-" * 26 + "\t\t\t" + "  " + "-" * 26)
        print(
            "d | {p1d1}  | {p1d2}  | {p1d3}  | {p1d4}  | {p1d5}  |\t\t\td | {p2d1}  | {p2d2}  | {p2d3}  | {p2d4}  | {p2d5}  |".format(
                **p1_positions, **p2_positions
            )
        )
        print("  " + "-" * 26 + "\t\t\t" + "  " + "-" * 26)
        print(
            "e | {p1e1}  | {p1e2}  | {p1e3}  | {p1e4}  | {p1e5}  |\t\t\te | {p2e1}  | {p2e2}  | {p2e3}  | {p2e4}  | {p2e5}  |".format(
                **p1_positions, **p2_positions
            )
        )
        print("  " + "-" * 26 + "\t\t\t" + "  " + "-" * 26)
        print(
            "  Player: {}\t\t\t  Player: {}".format(
                player_names[0].ljust(GameSetup.MAX_NAME), player_names[1]
            )
        )  # Fix spacing
        return None


class GameModeError(Exception):
    pass


class GameSetup:
    MAX_NAME: int = 18  # maximum number of characters allowed for a name

    @classmethod
    def set_max_name(cls: Type["GameSetup"], n_char: int) -> None:
        """
            ARGS
            ==========
                n_char: int; the maximun number of characters allowed for a name
            
            RETURNS
            ==========
                None.
        """
        cls.MAX_NAME = n_char
        return None

    @staticmethod
    def _select_game_mode() -> str:
        """
            ARGS
            ==========
                None.

            RETURNS
            ==========
                A string "single" or "double" indicating the game mode.
        """
        while True:
            Messages.info("Type 1 for one-player game or 2 for two-player game: ")
            answer: str = input()
            if answer.lower() == "1":
                Display.clear_monitor()
                return "single"
            elif answer.lower() == "2":
                Display.clear_monitor()
                return "double"
            else:
                Messages.error(
                    "Input must be 1 for single player or 2 for two players!"
                )

    @staticmethod
    def _get_player_names(mode: str) -> Tuple[str, str]:
        """
            ARGS
            ==========
                mode: str; the mode of the game. Can be "single" or "double".

            RETURNS
            ==========
                A tuple containing the players' names (when game mode is "double").
                If the game mode is "single" it returns a tuple that contains the 
                name of the player and the word "Computer" as the opponent's name.
        """
        print("-" * 40)
        print("\t Game Mode: {}".format(mode.capitalize()))
        print("-" * 40)
        if mode == "single":
            while True:
                player_1: str = input("Name of player: ").capitalize()
                if len(player_1) > GameSetup.MAX_NAME:
                    Messages.error(
                        "Player's name cannot exceed {} characters! Please try again.".format(
                            GameSetup.MAX_NAME
                        )
                    )
                elif player_1.isspace() or not player_1:
                    Messages.error("Player's name cannot be empty!")
                elif not player_1.isalpha():
                    Messages.error("All letters must be alphabets!")
                else:
                    break
            player_2: str = "Computer"
            Display.clear_monitor()
            return (player_1, player_2)
        elif mode == "double":
            while True:
                player_1 = input("Name of player 1: ").capitalize()
                if len(player_1) > GameSetup.MAX_NAME:
                    Messages.error(
                        "Player's name cannot exceed {} characters! Please try again.".format(
                            GameSetup.MAX_NAME
                        )
                    )
                elif player_1.isspace() or not player_1:
                    Messages.error("Player's name cannot be empty!")
                elif not player_1.isalpha():
                    Messages.error("All letters must be alphabets!")
                else:
                    break
            while True:
                player_2 = input("Name of player 2: ").capitalize()
                if len(player_2) > GameSetup.MAX_NAME:
                    Messages.error(
                        "Player's name cannot exceed {} characters! Please try again.".format(
                            GameSetup.MAX_NAME
                        )
                    )
                elif player_2.isspace() or not player_2:
                    Messages.error("Player's name cannot be empty!")
                elif not player_2.isalpha():
                    Messages.error("All letters must be alphabets!")
                else:
                    break
            Display.clear_monitor()
            return (player_1, player_2)
        else:
            raise GameModeError("game mode error")

    @staticmethod
    def _initialize_board(mode: str, names: Tuple[str, str]) -> Tuple[Set, Set]:
        """ 
            ARGS
            ==========
                mode: str; the mode of the game. Can be "single" or "double".
                names: tuple; the names of players

            RETURNS
            ==========
                A tuple that contains the ship positions of each player.
        """
        p1_positions: Set[str] = set()
        p2_positions: Set[str] = set()
        if mode == "single":
            for _ in range(5):
                while True:
                    candidate_square = random.choice(tuple(Positions.p2_grid.keys()))
                    if candidate_square not in p2_positions:
                        p2_positions.add(candidate_square)
                        break
            Display.board(Positions.p1_grid, Positions.p2_grid, names)
            Messages.info(
                f"{names[0].capitalize()}, please indicate the square you want to position your ship (e.g. a3, e5 etc)"
            )
            for num in range(1, 6):
                while True:
                    candidate_square = input(
                        f"Enter the position of your ship #{num}: "
                    ).lower()
                    if "".join(["p1", candidate_square]) in p1_positions:
                        Messages.error("There is already a ship in this position!")
                    elif candidate_square.isspace() or not candidate_square:
                        Messages.error("Position cannot be empty!")
                    elif Positions.position_is_valid(candidate_square):
                        p1_positions.add("p1" + candidate_square)
                        break
                    else:
                        Messages.error("This is an invalid position!")
            Display.clear_monitor()
            print("Good luck {}!".format(names[0]))
            print("=" * 80)
            return (p1_positions, p2_positions)
        elif mode == "double":
            Display.board(Positions.p1_grid, Positions.p2_grid, names)
            Messages.info(
                f"{names[0].capitalize()}, please indicate the square you want to position your ship (e.g. a3, e5 etc)"
            )
            Messages.warning(f"{names[1].capitalize()}, DON'T LOOK!")
            for num in range(1, 6):
                while True:
                    candidate_square = input(
                        f"Enter the position of your ship #{num}: "
                    ).lower()
                    if "".join(["p1", candidate_square]) in p1_positions:
                        Messages.error("There is already a ship in this position!")
                    elif candidate_square.isspace() or not candidate_square:
                        Messages.error("Position cannot be empty!")
                    elif Positions.position_is_valid(candidate_square):
                        p1_positions.add("p1" + candidate_square)
                        break
                    else:
                        Messages.error("This is an invalid position!")
            Display.clear_monitor()
            Display.board(Positions.p1_grid, Positions.p2_grid, names)
            Messages.info(
                f"{names[1].capitalize()}, please indicate the square you want to position your ship (e.g. a3, e5 etc)"
            )
            Messages.warning(f"{names[0].capitalize()}, DON'T LOOK!")
            for num in range(1, 6):
                while True:
                    candidate_square = input(
                        f"Enter the position of your ship #{num}: "
                    ).lower()
                    if "".join(["p2", candidate_square]) in p2_positions:
                        Messages.error("There is already a ship in this position!")
                    elif candidate_square.isspace() or not candidate_square:
                        Messages.error("Position cannot be empty!")
                    elif Positions.position_is_valid(candidate_square):
                        p2_positions.add("p2" + candidate_square)
                        break
                    else:
                        Messages.error("This is an invalid position!")
            Display.clear_monitor()
            print("Good luck {}, {}!".format(names[0], names[1]))
            print("=" * 80)
            return (p1_positions, p2_positions)
        else:
            raise GameModeError

    @dataclass
    class GameConfig:
        mode: str
        names: Tuple[str, str]
        positions: Tuple[Set, Set]

    @staticmethod
    def config() -> GameConfig:
        game_mode: str = GameSetup._select_game_mode()
        player_names: Tuple[str, str] = GameSetup._get_player_names(game_mode)
        occupied_positions: Tuple[Set, Set] = GameSetup._initialize_board(
            game_mode, player_names
        )
        return GameSetup.GameConfig(game_mode, player_names, occupied_positions)


class Positions:
    # The displayd grid for player 1
    p1_grid:Dict[str, str] = dict(
    p1a1 = ' ', p1a2 = ' ', p1a3 = ' ', p1a4 = ' ', p1a5 = ' ',
    p1b1 = ' ', p1b2 = ' ', p1b3 = ' ', p1b4 = ' ', p1b5 = ' ',
    p1c1 = ' ', p1c2 = ' ', p1c3 = ' ', p1c4 = ' ', p1c5 = ' ',
    p1d1 = ' ', p1d2 = ' ', p1d3 = ' ', p1d4 = ' ', p1d5 = ' ',
    p1e1 = ' ', p1e2 = ' ', p1e3 = ' ', p1e4 = ' ', p1e5 = ' '
    )

    # The displayed grid for player 2
    p2_grid:Dict[str, str] = dict(
    p2a1 = ' ', p2a2 = ' ', p2a3 = ' ', p2a4 = ' ', p2a5 = ' ',
    p2b1 = ' ', p2b2 = ' ', p2b3 = ' ', p2b4 = ' ', p2b5 = ' ',
    p2c1 = ' ', p2c2 = ' ', p2c3 = ' ', p2c4 = ' ', p2c5 = ' ',
    p2d1 = ' ', p2d2 = ' ', p2d3 = ' ', p2d4 = ' ', p2d5 = ' ',
    p2e1 = ' ', p2e2 = ' ', p2e3 = ' ', p2e4 = ' ', p2e5 = ' '
    )

    p1_attacked_positions: Set[str] = set() # Positions player 1 attacked
    p2_attacked_positions: Set[str] = set() # Positions player 2 attacked

    # Store original grids for resetting the game
    ORIG_GRID_CONFIG: Tuple[Dict, Dict] = (dict(p1_grid), dict(p2_grid))

    @staticmethod
    def reset_board(config=ORIG_GRID_CONFIG) -> None:
        Positions.p1_grid.update(config[0])
        Positions.p2_grid.update(config[1])

        Positions.p1_attacked_positions = set()
        Positions.p2_attacked_positions = set()
        return None

    @staticmethod
    def position_is_valid(square: str) -> bool:
        valid_squares: List[str] = [
            "a1", "a2", "a3", "a4", "a5",
            "b1", "b2", "b3", "b4", "b5",
            "c1", "c2", "c3", "c4", "c5",
            "d1", "d2", "d3", "d4", "d5",
            "e1", "e2", "e3", "e4", "e5"
        ]
        if square.lower() in valid_squares:
            return True
        else:
            return False


class Player:
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def plays_first(config: GameSetup.GameConfig) -> Type["Player"]:
        name: str = random.choice(config.names)
        Messages.info(f"\n{name} plays first!")
        return Player(name)

    @staticmethod
    def next_player(
        config: GameSetup.GameConfig, player: Type["Player"]
    ) -> Type["Player"]:
        if config.names[0] == player.name:
            Messages.info(f"\n{config.names[1]} plays next!")
            return Player(config.names[1])
        else:
            Messages.info(f"\n{config.names[0]} plays next!")
            return Player(config.names[0])

    def attack(self: Type["Player"], config: GameSetup.GameConfig) -> None:
        if config.mode == "single":
            if self.name == "Computer":
                while True:
                    attack_position: str = random.choice(
                        tuple(Positions.p1_grid.keys())
                    )
                    if attack_position not in Positions.p2_attacked_positions:
                        Positions.p2_attacked_positions.add(attack_position)
                        break
                    else:
                        attack_position = random.choice(tuple(Positions.p1_grid.keys()))

                if attack_position in config.positions[0]:
                    # print("Successful attack!")
                    Positions.p1_grid.update({attack_position: "o"})
                    config.positions[0].remove(attack_position)
                else:
                    # print("Target missed!")
                    Positions.p1_grid.update({attack_position: "x"})
            else:
                while True:
                    attack_position = input(
                        "Which position do you want to attack? (e.g. a1, e5 etc): "
                    )
                    if Positions.position_is_valid(attack_position):
                        break
                    else:
                        Messages.error("Invalid position! Try again:")

                while True:
                    attack_position = "".join(["p2", attack_position])
                    if attack_position not in Positions.p1_attacked_positions:
                        Positions.p1_attacked_positions.add(attack_position)
                        break
                    else:
                        Messages.error(
                            "You've already attacked this position! Try again:"
                        )
                        attack_position = input(
                            "Which position do you want to attack? (e.g. a1, e5 etc): "
                        )

                if attack_position in config.positions[1]:
                    # print("Successful attack!")
                    Positions.p2_grid.update({attack_position: "o"})
                    config.positions[1].remove(attack_position)
                else:
                    # print("Target missed!")
                    Positions.p2_grid.update({attack_position: "x"})
        else:
            while True:
                attack_position: str = input(
                    "Which position do you want to attack? (e.g. a1, e5 etc): "
                )
                if Positions.position_is_valid(attack_position):
                    break
                else:
                    Messages.error("Invalid position! Try again:")

            if self.name == config.names[0]:
                while True:
                    attack_position = "".join(["p2", attack_position])
                    if attack_position not in Positions.p1_attacked_positions:
                        Positions.p1_attacked_positions.add(attack_position)
                        break
                    else:
                        Messages.error(
                            "You've already attacked this position! Try again:"
                        )
                        attack_position = input(
                            "Which position do you want to attack? (e.g. a1, e5 etc): "
                        )

                if attack_position in config.positions[1]:
                    # print("Successful attack!")
                    Positions.p2_grid.update({attack_position: "o"})
                    config.positions[1].remove(attack_position)
                else:
                    # print("Target missed!")
                    Positions.p2_grid.update({attack_position: "x"})
            else:
                while True:
                    attack_position = "".join(["p1", attack_position])
                    if attack_position not in Positions.p2_attacked_positions:
                        Positions.p2_attacked_positions.add(attack_position)
                        break
                    else:
                        Messages.error(
                            "You've already attacked this position! Try again:"
                        )
                        attack_position = input(
                            "Which position do you want to attack? (e.g. a1, e5 etc): "
                        )

                if attack_position in config.positions[0]:
                    # print("Successful attack!")
                    Positions.p1_grid.update({attack_position: "o"})
                    config.positions[0].remove(attack_position)
                else:
                    # print("Target missed!")
                    Positions.p1_grid.update({attack_position: "x"})
        return None


class Game:
    @staticmethod
    def play(config: GameSetup.GameConfig) -> None:
        Display.board(Positions.p1_grid, Positions.p2_grid, config.names)
        current_player: Type["Player"] = Player.plays_first(config)
        while (config.positions[0] != set()) and (config.positions[1] != set()):
            print(config.positions[0])
            print(config.positions[1])
            if current_player.name == "Computer":
                sleep(2)
            current_player.attack(config)
            Display.clear_monitor()
            Display.board(Positions.p1_grid, Positions.p2_grid, config.names)
            current_player = Player.next_player(config, current_player)

        if config.positions[0] == set():
            # Display.board(Positions.p1_grid, Positions.p2_grid, config.names)
            Messages.info(f"{config.names[1]} wins!".upper())
        elif config.positions[1] == set():
            # Display.board(Positions.p1_grid, Positions.p2_grid, config.names)
            Messages.info(f"{config.names[0]} wins!".upper())
        return None


def main() -> None:
    Greetings.welcome()
    while True:
        config: GameSetup.GameConfig = GameSetup.config()
        Game.play(config)
        answer = input("Do you want to play again? (y/n): ")
        if answer.lower() == "n" or answer.lower() == "no":
            Greetings.goodbye()
            break
        elif answer.lower() == "y" or answer.lower() == "yes":
            Positions.reset_board()
            Display.clear_monitor()
        else:
            print("I didn't understand that! I'm exiting now...")
            Greetings.goodbye()
            break
    return None


if __name__ == "__main__":
    main()
