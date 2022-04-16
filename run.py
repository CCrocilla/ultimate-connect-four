""" Imports """
import sys
import random
import time
import numpy as np
from termcolor import (cprint,
                       colored)
from library import (Player,
                     Genres,
                     display_logo,
                     clear_console,
                     go_to_main_menu,
                     check_if_board_full,
                     check_horizontal_winner,
                     check_vertical_winner,
                     check_diagonal_winner,
                     check_move_horizontal,
                     check_move_vertical)


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


def instruction():
    """ Display the ASCII Instruction Logo and the Instructions """
    logo = "assets/files/instructions-logo.txt"
    rules = "assets/files/instructions-rules.txt"
    with open(logo, encoding="utf-8") as logo, \
            open(rules, encoding="utf-8") as rules:
        cprint(logo.read(), "red")
        cprint("\t\t\tInstructions\n", "red")
        cprint(rules.read())
    go_to_main_menu()
    main()


def restart_end_game():
    """ Reset the game and bring the user to the Main menu """
    let_r = colored("R", "cyan")
    let_e = colored("E", "cyan")
    msg_restart = (
        f"Do you want a [{let_r}]ematch or [{let_e}]xit the Game?\n")
    select_restart_end_game = input(msg_restart).lower()
    if select_restart_end_game == "r":
        reset_board()
    elif select_restart_end_game == "e":
        cprint("Thanks for playing Connect 4!" +
               " I hope to see you soon!\n", "green")
        sys.exit()
    else:
        cprint("This is not a valid option! Please try again!\n", "red")
        restart_end_game()


def reset_board():
    """ Function to reset the board """
    clear_console()
    cell = ""
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            board[row][col] = cell
    cprint("\nAre you ready for the rematch? The Board is Ready!", "cyan")
    render_board()
    players_turn(1, 2)


def render_board():
    """ Create and display the Board Game """
    lines = "-"
    end_lines = colored(" |", "blue")
    for row in range(BOARD_ROW):
        cprint(f"\n{lines * 50}", "blue")
        cprint("|", "blue", end="")
        for col in range(BOARD_COL):
            cell = board[row][col]
            if cell == "🟡" or cell == "🔴":
                print(f"  {cell}", end=f"  {end_lines}")
            else:
                print("  ", cell, end=f"  {end_lines}")
    cprint(f"\n{lines * 50}", "blue")
    cprint("\n    1      2      3      4      5      6      7\n", "blue")


def generate_input_cpu(coin, coin_enemy):
    """
    Function to generate with AI the choice of the CPU.
    If no valid AI option return a random value.
    """
    cpu_choice_col = 0

    position_h = check_move_horizontal(coin, coin_enemy, board, BOARD_ROW)
    if position_h is not None:
        cpu_choice_col = position_h[1] + 1
        return cpu_choice_col

    position_v = check_move_vertical(coin, coin_enemy, board, BOARD_COL)
    if position_v is not None:
        cpu_choice_col = position_v[1] + 1
        return cpu_choice_col

    if cpu_choice_col == 0:
        cpu_choice_col = random.randint(1, 7)
    return cpu_choice_col


def get_input(name, coin, coin_enemy, genre):
    """ Function to get the input for the board """
    if genre is Genres.HUMAN:
        input_player = get_input_human(name, coin)
    elif genre is Genres.CPU:
        input_player = get_input_cpu(name, coin, coin_enemy)
    else:
        cprint("Error: This genre is not available." +
               " Please restart the game!", "red")
        sys.exit()
    return input_player


def get_input_cpu(name, coin, coin_enemy):
    """ Function to get input from player """
    input_player = generate_input_cpu(coin, coin_enemy)
    input_player -= 1
    cprint(f"{name} is thinking...", "cyan")
    time.sleep(4)
    clear_console()
    cprint(f"\n{name} has picked the column: {input_player+1}!", "cyan")
    return input_player


def get_input_human(name, coin):
    """ Function to get input from cpu """
    input_player = int(input(
                f"{name} it's your turn {coin} !" +
                " Pick a column from 1 to 7: \n"))
    input_player -= 1
    time.sleep(0.3)
    clear_console()
    cprint(f"\n{name} has picked the column: {input_player+1}!", "green")
    return input_player


def check_valid_move(input_player, next_turn, prev_turn):
    """ Check if the input_player is valid """
    coin_row_insert = -1
    if input_player in range(0, BOARD_COL):
        time.sleep(0.3)
        coin_row_insert = get_row_insert(input_player)
    else:
        cprint("The column number entered is not valid." +
               " Please try again!", "red")
        render_board()
        players_turn(next_turn, prev_turn)
    return coin_row_insert


def check_board(name, coin, next_turn):
    """ Check the board for winners or pair """
    if check_game_over(name, coin):
        render_board()
        time.sleep(0.3)
        restart_end_game()
    else:
        move_forward(next_turn)


def players_turn(next_turn, prev_turn):
    """ Function to pick insert users/cpu. Check Game Over/Winner """
    coin_row_insert = -1
    input_player = -1
    coin = players[next_turn-1].coin
    coin_enemy = players[prev_turn-1].coin
    name = players[next_turn-1].name
    genre = players[next_turn-1].genre
    try:
        input_player = get_input(name, coin, coin_enemy, genre)
        coin_row_insert = check_valid_move(input_player, next_turn, prev_turn)
        if coin_row_insert != -1:
            insert_value_matrix(coin_row_insert, input_player, coin)
            check_board(name, coin, next_turn)
        else:
            if genre is Genres.HUMAN:
                cprint("Sorry but the column is full!" +
                       " Please pick a new one!\n", "red")
            players_turn(next_turn, prev_turn)
    except ValueError:
        cprint("\nError: The value entered is not allowed." +
               " Please try again!\n", "red")
        players_turn(next_turn, prev_turn)


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
    """ Function to insert value in the Matrix """
    board[row][col] = coin


def move_forward(prev_turn):
    """ Function to determinate the turn of the player """
    next_turn = 0
    if prev_turn == 1:
        next_turn = 2
    else:
        next_turn = 1
    render_board()
    players_turn(next_turn, prev_turn)


def check_game_over(name, coin):
    """ Function that check if the game is ended """
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
    let_s = colored("S", "cyan")
    let_m = colored("M", "cyan")
    msg_start_game = (
        f"Do you want to play [{let_s}]ingle or [{let_m}]ultiplayer Mode?\n")
    cprint("\nAre you ready for the Ultimate Connect 4 Battle?\n", "cyan")
    select_mode = input(msg_start_game).lower()
    if select_mode == "s":
        players.append(Player("", 1, "🟡", Genres.HUMAN))
        players.append(Player("Roboto", 2, "🔴", Genres.CPU))
        players[0].input_info()
        players[0].print_info()
        cprint("Great! The Board is ready!!!" +
               " Roboto is your opponent! Let's Play!!!", "green")
        render_board()
        players_turn(1, 2)
    elif select_mode == "m":
        players.append(Player("", 1, "🟡", Genres.HUMAN))
        players.append(Player("", 2, "🔴", Genres.HUMAN))
        for player in players:
            player.input_info()
            player.print_info()
        cprint("Great! The Board is ready!!!" +
               " Let's Play!!!", "green")
        render_board()
        players_turn(1, 2)
    else:
        cprint("\nInvalid Selection! Please select a valid option!\n", "red")
        start_game()


def start_menu():
    """
    Ask to the user if they want to Start Playing
    or read the Instructions.
    """
    let_p = colored("P", "cyan")
    let_i = colored("I", "cyan")
    msg_start_menu = (
        f"Do you want to [{let_p}]lay or read the [{let_i}]nstructions?\n")
    cprint("\n\t\tWelcome to Connect 4\n", "red")
    selection = input(msg_start_menu).lower()
    if selection == "p":
        clear_console()
        display_logo()
        start_game()
    elif selection == "i":
        clear_console()
        instruction()
    else:
        cprint("\nInvalid Selection! Please select a valid option!\n", "red")
        main()


def main():
    """
    Start all initial programs
    """
    display_logo()
    start_menu()


main()
