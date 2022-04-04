import os
import random
import numpy as np
from pprint import pprint 
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
    def __init__(self, name, turn, coin, genre):
        self.name = name
        self.turn = turn
        self.coin = coin
        self.genre = genre

    def input_info(self):
        self.name = input(f"Player {self.turn} what's your name?\n")
        cprint(f"\nHi {self.name}! Welcome in Ultimate Connect 4!", "cyan")

    def print_info(self):
        print(f"\n{self.name} your turn is: {self.turn} and your coin will be {self.coin}!\n")


def logo():
    """
    Display the ASCII Logo
    """
    logo = open("assets/files/logo.txt")
    cprint(logo.read(), "red")
    logo.close()


def pause():
    """
    Pause until the user press Enter
    """
    input("Press the [ENTER] key to return Home...\n")


def clear_console():
    """ 
    Clear the Console Terminal
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def reset_game():
    pause()
    clear_console()
    #TODO: Add reset board. For or Delete Numpy.
    reset_board()
    main()


def reset_board():
    np.delete(board, [0,0], axis = 0)


def instruction():
    """
    Display the ASCII Instruction Logo and the Instructions
    """
    instruction_logo = open("assets/files/instructions-logo.txt")
    cprint(instruction_logo.read(), "red")
    instruction_logo.close()
    cprint("                   Instructions\n", "red")
    instruction_rules = open("assets/files/instructions-rules.txt")
    cprint(instruction_rules.read())
    instruction_rules.close()
    reset_game()


def render_board():
    """
    Create and display the Board Game
    """
    for row in range(BOARD_ROW):
        cprint("\n--------------------------------------------------------", "blue")
        for col in range(BOARD_COL):
            cell = board[row][col]
            if cell == "":
                cell = "  "
            cprint(f"|  {cell}  |", "blue", end="")                
    cprint("\n--------------------------------------------------------", "blue")
    cprint("\n    0       1       2       3       4       5       6\n", "blue")


#TODO: For CPU Check which Columns are available
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
        input_player = int(input(f"{name} it's your turn! Pick a column from 0 to 5: \n"))
    elif genre == "cpu":
        input_player = get_input_cpu()
    else:
        cprint("Error: This genre is not available. Please restart the game!")
        exit()
    
    if input_player != "" and input_player >= 0 and input_player <= 6:
        coin_row_to_insert = get_row_insert(input_player)
    else:
        print("The column number entered is not valid. Please try again!")
        players_turn(next_turn)
        
    if coin_row_to_insert != -1:
        insert_value_matrix(coin_row_to_insert, input_player, coin)
        if check_game_over():
            render_board()
            reset_game()
        elif check_for_winner(next_turn, name, coin):
            render_board()
            reset_game()   
        else:
            move_forward(next_turn)
    else:
        print("Sorry but the column is full! Please pick a new one!")
        players_turn(next_turn)


def get_row_insert(input_player):
    """ Function to realize the gravity for the Coins """
    row_ins = -1
    for row in range(BOARD_ROW):
        cell = board[BOARD_ROW - row -1][input_player]
        if cell == "":
            row_ins = BOARD_ROW - row -1
            break
    return row_ins


def insert_value_matrix(row, col, coin):
    """
    Function to insert value in the Matrix!
    """
    board[row][col] = coin
    
      
#TODO: Checks End Game
def check_game_over():
    game_over = False
    game_over = check_if_board_full()
    #TODO: Check for winner 
    return game_over


def check_if_board_full():
    """ Check all the string in the array """
    if any("" in element for element in board):
        return False
    else:
        cprint("Game Over! The Board is full! This is a tie!", "red")
        return True


def check_for_winner(next_turn, name, coin):
    """Horizontal/Vertical/Diagonal"""
    #coin = players[next_turn-1].coin
    #name = players[next_turn-1].name
    #for row in range(BOARD_ROW):
    #    for col in range(BOARD_COL):
    #        if board[row][col] == "🟡":
    #            coin += 1
    #            print("this is the value of the yellow coin:", coin) 
    for col in range(4):
        for row in range(BOARD_ROW):
            if board[row][col] == coin and board[row][col+1] == coin and board[row][col+2] == coin and board[row][col+3] == coin:
                cprint(f"{name} you are the WINNER!!!", "yellow")
                return True


def check_for_winner_diagonal():
    board = np.arange(42).reshape((6,7))
    np.diag(np.diag(board))
    print(board)


def move_forward(prev_turn):
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
    select_mode = input("Do you want to play in [S]ingle or [M]ultiplayer Mode?\n").lower()
    if select_mode == "s":
        players.append(Player("", 1, "🟡", "human"))
        players.append(Player("Roboto", 2, "🔴", "cpu"))
        players[0].input_info()
        players[0].print_info()
        print("Great! The Board is ready!!! Let's Play!!!")
        print("")
        render_board()
        players_turn(1)
    elif select_mode == "m":
        # TO DO: Input Player Info
        players.append(Player("", 1, "🟡", "human"))
        players.append(Player("", 2, "🔴", "human"))
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
    cprint("               Welcome to Connect 4\n", "red")
    selection = input("Do you want to [P]lay or read the [I]nstructions?\n").lower()
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
    logo()
    start_menu()


main()