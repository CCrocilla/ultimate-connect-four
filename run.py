""" Import """
import sys
import random
import shutil
import time
from enum import Enum
import numpy as np
from termcolor import cprint, colored
from library.utilities import (clear_console,
                               go_to_main_menu
                               )
from library.gameover import (check_if_board_full,
                              check_horizontal_winner,
                              check_vertical_winner,
                              check_diagonal_winner
                              )


BOARD_ROW = 6
BOARD_COL = 7
players = []
board = np.array([
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
])

#columns = shutil.get_terminal_size().columns
#TEXT_PYTHON = "Python is awsome".center(columns, "^")
#print(TEXT_PYTHON)
#test = colored("test", 'cyan')
#print(f"This is a {test}".center(columns))
#cprint(f"This is a {test} of Test".center(columns), "red")


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
            self.name = input(f"Player {self.turn} what's your name?\n")
            clear_console()
            display_logo()
            cprint(f"\nHi {self.name}! Welcome in Ultimate Connect 4!", "cyan")
        except ValueError:
            cprint("\nHi! This is not a valid input! Please try again!\n", "red")
            Player.input_info(self)

    def print_info(self):
        """ Display Information to the user about turn and coin """
        print(
            f"\n{self.name} your turn is: {self.turn} and your coin is {self.coin}!\n")


class Genres(Enum):
    """ Class for the Player Genre """
    HUMAN = "human"
    CPU = "cpu"


def display_logo():
    """ Display the ASCII Logo """
    with open("assets/files/logo.txt", encoding="utf-8") as logo:
        main_menu = logo.read()
        cprint(main_menu, "red")


def instruction():
    """ Display the ASCII Instruction Logo and the Instructions """
    logo = "assets/files/instructions-logo.txt"
    rules = "assets/files/instructions-rules.txt"
    with open(logo, encoding="utf-8") as logo, open(rules, encoding="utf-8") as rules:
        cprint(logo.read(), "red")
        cprint("\t\t\tInstructions\n", "red")
        cprint(rules.read())
    go_to_main_menu()
    main()


def restart_end_game():
    """ Reset the game and bring the user to the Main menu """
    let_r = colored("R", 'cyan')
    let_e = colored("E", 'cyan')
    message_restart = f"Do you want to play the [{let_r}]ematch or [{let_e}]xit the Game?\n"
    select_restart_end_game = input(message_restart).lower()
    if select_restart_end_game == "r":
        clear_console()
        reset_board()
        cprint("Are you ready for the rematch? The Board is Ready!\n", "cyan")
        render_board()
        players_turn(1)
    elif select_restart_end_game == "e":
        cprint("Thanks for playing Connect 4! I hope to see you soon!\n", "green")
        sys.exit()
    else:
        cprint("This is not a valid option! Please try again!\n", "red")
        restart_end_game()


def reset_board():
    """ Function to reset the board """
    cell = ""
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            board[row][col] = cell


def render_board():
    """ Create and display the Board Game """
    lines = "-"
    for row in range(BOARD_ROW):
        cprint(f"\n{lines * 56}", "blue")
        for col in range(BOARD_COL):
            cell = board[row][col]
            if cell == "":
                cell = "  "
            cprint(f"|  {cell}  |", "blue", end="")
    cprint(f"\n{lines * 56}", "blue")
    cprint("\n    0       1       2       3       4       5       6\n", "blue")


# TO DO: For CPU Check which Columns are available
def get_input_cpu():
    """ Function to get the cpu random input """
    cpu_choice_col = random.randint(0, 6)
    return cpu_choice_col


def players_turn(next_turn):
    """ Function to pick insert users/cpu. Check Game Over/Winner """
    coin = players[next_turn-1].coin
    name = players[next_turn-1].name
    genre = players[next_turn-1].genre
    coin_row_to_insert = -1
    input_player = -1
    try:
        if genre is Genres.HUMAN:
            input_player = int(
                input(f"{name} it's your turn {coin} ! Pick a column from 0 to 6: \n"))
            time.sleep(0.3)
            clear_console()
            cprint(f"{name} has picked the column: {input_player}!", "green")
        elif genre is Genres.CPU:
            input_player = get_input_cpu()
            cprint(f"{name} is thinking!", "magenta")
            time.sleep(3.5)
            clear_console()
            cprint(f"{name} has picked the column: {input_player}!", "magenta")
        else:
            cprint("Error: This genre is not available. Please restart the game!", "red")
            sys.exit()

        if input_player in range(0, BOARD_COL):
            time.sleep(0.3)
            coin_row_to_insert = get_row_insert(input_player)
        else:
            cprint("The column number entered is not valid. Please try again!", "red")
            render_board()
            players_turn(next_turn)

        if coin_row_to_insert != -1:
            insert_value_matrix(coin_row_to_insert, input_player, coin)
            if check_game_over(name, coin):
                render_board()
                time.sleep(0.3)
                restart_end_game()
            else:
                move_forward(next_turn)
        else:
            if genre is Genres.HUMAN:
                cprint("Sorry but the column is full! Please pick a new one!\n", "red")
            players_turn(next_turn)
    except ValueError:
        cprint("\nThe value is not a valid input. Please try again!\n", "red")
        players_turn(next_turn)


def get_row_insert(input_player):
    """ Function to realize the gravity for the Coins """
    row_ins = -1
    for row in range(BOARD_ROW):
        cell = board[BOARD_ROW - row - 1][input_player]
        if cell == "":
            row_ins = BOARD_ROW - row - 1
            break
    return row_ins


def insert_value_matrix(row, col, coin):
    """ Function to insert value in the Matrix! """
    board[row][col] = coin


def move_forward(prev_turn):
    """ Function to determinate the turn of the player """
    next_turn = 0
    if prev_turn == 1:
        next_turn = 2
    else:
        next_turn = 1
    render_board()
    players_turn(next_turn)


def check_game_over(name, coin):
    """ Function that check if the game is ended """
    game_over = False
    game_over = check_if_board_full(board) or \
        check_horizontal_winner(board, name, coin, BOARD_ROW) or \
        check_vertical_winner(board, name, coin, BOARD_COL) or \
        check_diagonal_winner(board, name, coin)
    return game_over


def start_game():
    """
    Request to the user the mode(Single Player or Multiplayer).
    Ask for the Username(s) and Print the information.
    """
    let_s = colored("S", 'cyan')
    let_m = colored("M", 'cyan')
    message_start_game = f"Do you want to play in [{let_s}]ingle or [{let_m}]ultiplayer Mode?\n"
    cprint("\n   Are you ready for the Ultimate Connect 4 Battle?\n", "cyan")
    select_mode = input(message_start_game).lower()
    if select_mode == "s":
        players.append(Player("", 1, "🟡", Genres.HUMAN))
        players.append(Player("Roboto", 2, "🔴", Genres.CPU))
        players[0].input_info()
        players[0].print_info()
        cprint("Great! The Board is ready!!! Roboto is your opponent! Let's Play!!!\n", "green")
        render_board()
        players_turn(1)
    elif select_mode == "m":
        players.append(Player("", 1, "🟡", Genres.HUMAN))
        players.append(Player("", 2, "🔴", Genres.HUMAN))
        for player in players:
            player.input_info()
            player.print_info()
        cprint("Great! The Board is ready!!! Let's Play!!!\n", "green")
        render_board()
        players_turn(1)
    else:
        cprint("\nInvalid Selection! Please select one of the valid options!\n", "red")
        start_game()


def start_menu():
    """
    Ask to the user if they want to Start Playing
    or read the Instructions.
    """
    let_p = colored("P", 'cyan')
    let_i = colored("I", 'cyan')
    message_start_menu = f"Do you want to [{let_p}]lay or read the [{let_i}]nstructions?\n"
    cprint("\n\t\tWelcome to Connect 4\n", "red")
    selection = input(message_start_menu).lower()
    if selection == "p":
        clear_console()
        display_logo()
        start_game()
    elif selection == "i":
        clear_console()
        instruction()
    else:
        cprint("\nInvalid Selection! Please select one of the valid options!\n", "red")
        main()


def main():
    """
    Start all initial programs
    """
    display_logo()
    start_menu()


main()
