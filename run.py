""" Import """
import os
import random
from enum import Enum
import numpy as np
from termcolor import cprint


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
        self.name = input(f"Player {self.turn} what's your name?\n")
        cprint(f"\nHi {self.name}! Welcome in Ultimate Connect 4!", "cyan")

    def print_info(self):
        """ Display Information to the user about turn and coin """
        print(
            f"\n{self.name} your turn is: {self.turn} and your coin will be {self.coin}!\n")


class Genres(Enum):
    """ Class for the Player Genre """
    HUMAN = "human"
    CPU = "cpu"


def display_logo():
    """ Display the ASCII Logo """
    with open("assets/files/logo.txt", encoding="utf-8") as logo:
        main_menu = logo.read()
        cprint(main_menu, "red")


def pause():
    """ Pause until the user press Enter """
    input("Press the [ENTER] key to return Home...\n")


def clear_console():
    """ Clear the Console Terminal """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # "cls" if is running on Windows
        command = 'cls'
    os.system(command)


def go_to_main_menu():
    """ Return to the Main Menu """
    pause()
    clear_console()
    main()


def restart_end_game():
    """ Reset the game and bring the user to the Main menu """
    select_restart_end_game = input(
        "Do you want to play the [R]ematch or [E]xit the Game?\n").lower()
    if select_restart_end_game == "r":
        clear_console()
        reset_board()
        print("Are you ready for the rematch? The Board is Ready!\n")
        render_board()
        players_turn(1)
    elif select_restart_end_game == "e":
        print("Thanks for playing Connect 4! I hope to see you soon!\n")
        exit()
    else:
        cprint("This is not a valid option! Please try again!\n", "red")
        restart_end_game()


def reset_board():
    """ Function to reset the board """
    cell = ""
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            board[row][col] = cell


def instruction():
    """ Display the ASCII Instruction Logo and the Instructions """
    logo = "assets/files/instructions-logo.txt"
    rules = "assets/files/instructions-rules.txt"
    with open(logo, encoding="utf-8") as logo, open(rules, encoding="utf-8") as rules:
        cprint(logo.read(), "red")
        cprint("\t\t\tInstructions\n", "red")
        cprint(rules.read())
    go_to_main_menu()


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
    #cprint("\n\t0\t1\t2\t3\t4\t5\t6\n", "blue")


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
    if genre == "human":
        input_player = int(
            input(f"{name} it's your turn! Pick a column from 0 to 5: \n"))
    elif genre == "cpu":
        input_player = get_input_cpu()
        cprint(f"{name} has picked the column: {input_player}!", "magenta")
    else:
        cprint("Error: This genre is not available. Please restart the game!", "red")
        exit()

    if input_player != "" and input_player >= 0 and input_player <= 6:
        coin_row_to_insert = get_row_insert(input_player)
    else:
        cprint("The column number entered is not valid. Please try again!", "red")
        players_turn(next_turn)

    if coin_row_to_insert != -1:
        insert_value_matrix(coin_row_to_insert, input_player, coin)
        if check_game_over(name, coin):
            render_board()
            restart_end_game()
        else:
            move_forward(next_turn)
    else:
        if genre == "human":
            print("Sorry but the column is full! Please pick a new one!")
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


# TO DO: Checks End Game
def check_game_over(name, coin):
    """ Function that check if the game is ended """
    game_over = False
    game_over = check_if_board_full()
    game_over = check_for_winner(name, coin)
    return game_over


def check_if_board_full():
    """
    Check if any of the string in the array is empty.
    If there is no empty string in the array then return
    True value and the game is over as tie
    """
    if any("" in element for element in board):
        return False
    else:
        cprint("Game Over! The Board is full! This is a tie!", "red")
        return True


def check_for_winner(name, coin):
    """ Check for the Horizontal/Vertical/Diagonal Winner """
    #Check for Horizontal Winner
    for col in range(4):
        for row in range(BOARD_ROW):
            if board[row][col] == board[row][col+1] == \
                board[row][col+2] == board[row][col+3] == coin:
                cprint(f"🎉 {name} you are the WINNER!!! Congratulations!!! 🎉", "yellow")
                return True

    # Check for Vertical Winner
    for col in range(BOARD_COL):
        for row in range(3):
            if board[row][col] == board[row+1][col] == \
                board[row+2][col] == board[row+3][col] == coin:
                cprint(f"🎉 {name} you are the WINNER!!! Congratulations!!! 🎉", "yellow")
                return True

    #Check for Diagonal Winner
    for col in range(4):
        for row in range(3):
            if board[row][col] == board[row+1][col+1] == \
                board[row+2][col+2] == board[row+3][col+3] == coin:
                cprint(f"🎉 {name} you are the WINNER!!! Congratulations!!! 🎉", "yellow")
                return True

    #Check for Negative Diagonal Winner
    for col in range(4):
        for row in range(5, 2, -1):
            if board[row][col] == board[row-1][col+1] == \
                board[row-2][col+2] == board[row-3][col+3] == coin:
                cprint(f"🎉 {name} you are the WINNER!!! Congratulations!!! 🎉", "yellow")
                return True


def move_forward(prev_turn):
    """ Function to determinate the turn of the player """
    next_turn = 0
    if prev_turn == 1:
        next_turn = 2
    else:
        next_turn = 1
    render_board()
    players_turn(next_turn)


def start_game():
    """
    Request to the user the mode(Single Player or Multiplayer)
    and ask for the Usernames
    """
    print("Are you ready for the Ultimate Connect 4 Battle?\n")
    select_mode = input(
        "Do you want to play in [S]ingle or [M]ultiplayer Mode?\n").lower()
    if select_mode == "s":
        players.append(Player("", 1, "🟡", Genres.HUMAN.value)) #TO DO: Enums instead "human".
        players.append(Player("Roboto", 2, "🔴", Genres.CPU.value)) #TO DO: Enums instead "cpu".
        players[0].input_info()
        players[0].print_info()
        print("Great! The Board is ready!!! Let's Play!!!")
        print("")
        render_board()
        players_turn(1)
    elif select_mode == "m":
        players.append(Player("", 1, "🟡", Genres.HUMAN.value))
        players.append(Player("", 2, "🔴", Genres.HUMAN.value))
        for player in players:
            player.input_info()
            player.print_info()
        print("Great! The Board is ready!!! Let's Play!!!")
        print("")
        render_board()
        players_turn(1)
    else:
        cprint("This is not a valid option! Please try again!\n", "red")
        start_game()


def start_menu():
    """
    Ask to the user if they want to Start Playing
    or read the Instructions.
    """
    cprint("\n\t\tWelcome to Connect 4\n", "red")
    selection = input(
        "Do you want to [P]lay or read the [I]nstructions?\n").lower()
    if selection == "p":
        start_game()
    elif selection == "i":
        clear_console()
        instruction()
    else:
        print("Invalid Selection")
        main()


def main():
    """
    Start all initial programs
    """
    display_logo()
    start_menu()


main()
