""" Imports """
from enum import Enum
from termcolor import cprint
from library.utilities import (clear_console,
                               display_logo
                               )


class Player:
    """
    Class Player for the management of the Players information.
    """
    def __init__(self, name, turn, coin, genre):
        self.name = name
        self.turn = turn
        self.coin = coin
        self.genre = genre

    def input_info(self):
        """ Request name to the user(s) """
        try:
            self.name = input(f"Player {self.turn}, what's your name?\n")
            clear_console()
            display_logo()
            cprint(f"\nHi {self.name}! Welcome in Ultimate Connect 4!", "cyan")
        except ValueError:
            cprint("\nThis is not a valid input! Please try again!\n", "red")
            Player.input_info(self)

    def print_info(self):
        """ Display Information to the user about turn and coin """
        print(
            f"\n{self.name} your turn is {self.turn}" +
            f" and your coin is {self.coin}!\n")


class Genres(Enum):
    """ Class for the Player Genre """
    HUMAN = "human"
    CPU = "cpu"
