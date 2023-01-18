"""
rock_paper_scissors.py

A simole Python approach to play the classic rock-paper-scissors game.
It supports one game mode:
    - Single mode      : one player against the computer
@author: Savvas Chanlaridis
@version: v2023-01-18
"""

import random
import os
from time import sleep

try:
    from typing import Dict, Optional
    from termcolor import colored
except ImportError:
    os.system("pip install typing")
    from typing import Dict, Optional

    os.system("python3 -m pip install --upgrade termcolor")
    from termcolor import colored


class Messages:
    @staticmethod
    def message(text: str, color: str) -> None:
        print(colored(text, color))
        return None

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

    @staticmethod
    def welcome() -> None:
        """
        It prints out a welcome message.
        """
        print("\n")
        print("\t\t\t" + "#" * 39)
        print("\t\t\t#" + " " * 37 + "#")
        print(
            "\t\t\t#"
            + " " * 3
            + colored("WELCOME TO ROCK-PAPER-SCISSORS!", "cyan")
            + " " * 3
            + "#"
        )
        print("\t\t\t#" + " " * 37 + "#")
        print("\t\t\t" + "#" * 39)
        print("\n")
        print("\t\t\t\t\t" + "-" * 5)
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
        Messages.warning("Clearing the monitor...")
        if os.name == "nt":
            sleep(delay_sec)
            os.system("cls")
        else:
            sleep(delay_sec)
            os.system("clear")
    return None


def main() -> None:
    RPS_SCHEMA: Dict[int, str] = {1: "Rock", 2: "Paper", 3: "Scissors"}
    Messages.welcome()
    while True:
        cpu_choice: str = RPS_SCHEMA[random.randint(1, 3)]

        while True:
            try:
                Messages.info("Select one of the following numbers:")
                Messages.message("1 (Rock), 2 (Paper), 3 (Scissors)", "magenta")
                user_number: int = int(input())
                user_choice: str = RPS_SCHEMA[user_number]
                break
            except (KeyError, ValueError):
                Messages.error("Input must be 1, 2, or 3!\n")
            except Exception as e:
                Messages.error(
                    str(e)
                )  # cast Exception to string to stop mypy complaining

        if cpu_choice == "Rock" and user_choice == "Paper":
            Messages.info("Computer chose Rock! You Win!")
        elif cpu_choice == "Paper" and user_choice == "Paper":
            Messages.info("Computer chose Paper! It's a Tie!")
        elif cpu_choice == "Scissors" and user_choice == "Paper":
            Messages.info("Computer chose Scissors! You Lose!")
        elif cpu_choice == "Rock" and user_choice == "Rock":
            Messages.info("Computer chose Rock! It's a Tie!")
        elif cpu_choice == "Paper" and user_choice == "Rock":
            Messages.info("Computer chose Paper! You Lose!")
        elif cpu_choice == "Scissors" and user_choice == "Rock":
            Messages.info("Computer chose Scissors! You Win!")
        elif cpu_choice == "Rock" and user_choice == "Scissors":
            Messages.info("Computer chose Rock! You Lose!")
        elif cpu_choice == "Paper" and user_choice == "Scissors":
            Messages.info("Computer chose Paper! You Win!")
        elif cpu_choice == "Scissors" and user_choice == "Scissors":
            Messages.info("Computer chose Scissors! It's a Tie!")
        else:
            Messages.warning("Something went wrong!")

        answer: str = input("Do you want to play again [y/n]? ")
        if answer.lower() == "y" or answer.lower() == "yes":
            clear_monitor()
        elif answer.lower() == "n" or answer.lower() == "no":
            Messages.goodbye()
            break
        else:
            Messages.warning("I didn't understand that! I'm exiting now...")
            Messages.goodbye()
            break
    return None


if __name__ == "__main__":
    main()
