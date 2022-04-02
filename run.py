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
    ["", "", "", "", "", "", ""],
])
      

class Player:
    def __init__(self, name, turn, coin, type):
        self.name = name
        self.turn = turn
        self.coin = coin
        self.type = type
        
    def update_info(self, name, turn, coin):
        self.name = name
        self.turn = turn
        self.coin = coin
        
    def input_info(self):
        self.name = input(f"Player {self.turn} what's your name?\n")
        print(f"Hi {self.name}!\n")
        
    def print_info(self):
        print(f"Hi {self.name} your turn is: {self.turn} and your coin will be {self.coin}!")
              

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
    pause()
    clear_console()
    main()


def render_board():
    """
    Create and display the Board Game
    """
    for row in range(BOARD_ROW):
        cprint("\n-------------------------------------------", "blue")
        for col in range(BOARD_COL):
            cell = board[row][col]
            if cell == "":
                cell = "  "
            cprint(f"|  {cell}  ", "blue", end="")                
    cprint("\n-------------------------------------------", "blue")
    cprint("\n    0      1      2      3      4      5", "blue")
    print("") 
    
    
def cpu_turn():
    coin = "🔴"
    cpu_choice_row = random.randint(0, 6)
    cpu_choice_col = random.randint(0, 5)
    print(cpu_choice_row, cpu_choice_col)
    insert_value_matrix(cpu_choice_row, cpu_choice_col, coin) 
       

def players_turn(player):
    if player == 1:
        player += 1
        input_player_one = int(input(f"{player} it is your turn! Pick a column from 0 to 5: "))
        player_one_turn(input_player_one)
    else:
        print("Player 2")


def player_one_turn(input_player_one):
    row_to_insert = -1
    for row in range(BOARD_ROW):
        if input_player_one != "" and input_player_one >= 0 and input_player_one <= 5:
            cell = board[BOARD_ROW - row -1][input_player_one]
            print(cell)
            if cell == "":
                row_to_insert = BOARD_ROW - row -1
                break
        else:
            print("The column number entered is not valid. Please try again!")
            player_one_turn()
    coin = "🟡"
    if row_to_insert != -1:
        insert_value_matrix(row_to_insert, input_player_one, coin)
    else:
        print("Sorry but the column is full! Please pick a new one!")
        player_one_turn()


def insert_value_matrix(row, col, coin):
    """
    Function to insert value in the Matrix!
    """
    player_turn = 0
    print(f"{row} and the column: {col}")
    if (player_turn % 2) != 1:
        player_turn += 1
        coin = "🟡"
        print(f"Here the coin {coin}")
        board[row][col] = coin
        render_board()
        players_turn()
    else:
        player_turn += 1
        coin = "🔴"
        print(f"Here the coin {coin}")
        board[row][col] = coin
        render_board()
        players_turn()


def start_game():
    """
    Request to the user the mode(Single Player or Multiplayer)
    and ask for the Usernames
    """
    print("Are you ready for the Ultimate Connect 4 Battle?\n")
    select_mode = input("Do you want to play in [S]ingle or [M]ultiplayer Mode?\n").lower()
    if select_mode == "s":
        cprint("Wrong choise! This option is not available yet! Try again! \n", "red")
        start_game()
    elif select_mode == "m":
        # TO DO: Input Player Info
        players = [Player("", 1, "🟡", "human"), Player("", 2, "🔴", "human")]
        for player in players:
            player.input_info() 
            player.print_info()
        print("Great! Are you ready?! The Board is ready!!!")
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