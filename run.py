import os
import random
import numpy as np
from pprint import pprint 
from termcolor import cprint


BOARD_ROW = 6
BOARD_COL = 7
player_one_name = ""
player_two_name = ""
board = np.array([
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
])



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


def create_board():
    """
    Create and display the Board Game
    """
    player = 0
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
    if (player % 2) == 0:
        player += 1
        player_one_turn()
    else:
        player += 1
        player_two_turn()
    
    
def cpu_turn():
    chip = "🔴"
    cpu_choice_row = random.randint(0, 6)
    cpu_choice_col = random.randint(0, 5)
    print(cpu_choice_row, cpu_choice_col)
    insert_value_matrix(cpu_choice_row, cpu_choice_col, chip) 
       

def player_one_turn():
    row_to_insert = -1
    input_player_one = int(input("Player 1 it is your turn! Pick a column from 0 to 5: "))
    print(f"Player have entered the chip in column: {input_player_one}")
    for row in range(BOARD_ROW):
        print(row)
        if input_player_one != "" and input_player_one >= 0 and input_player_one <= 5:
            cell = board[row][input_player_one]
            if cell == "":
                row_to_insert = row
                break
        else:
            print("The column number entered is not valid. Please try again!")
            player_one_turn()
    chip = "🟡"
    if row_to_insert != -1:
        insert_value_matrix(row_to_insert, input_player_one, chip)
    else:
        print("Sorry but the column is full! Please pick a new one!")
        player_one_turn()


def player_two_turn():
    row_to_insert = -1
    input_player_two = int(input("Player 2 it is your turn! Pick a column from 0 to 5: "))
    print(f"Player have entered the chip in column: {input_player_two}")
    for row in range(BOARD_ROW):
        print(row)
        if input_player_two != "" and input_player_two >= 0 and input_player_two <= 5:
            cell = board[row][input_player_two]
            if cell == "":
                row_to_insert = row
                break
        else:
            print("The column number entered is not valid. Please try again!")
            player_two_turn()
    chip = "🔴"
    if row_to_insert != -1:
        insert_value_matrix(row_to_insert, input_player_two, chip)
    else:
        print("Sorry but the column is full! Please pick a new one!")
        player_two_turn()


def insert_value_matrix(row, col, chip):
    """
    Function to insert value in the Matrix!
    """
    player_turn = 0
    if (player_turn % 2) != 1:
        player_turn += 1
        chip = "🟡"
        print(f"Here the chip {chip}")
        board[row][col] = chip
        create_board()
    else:
        player_turn += 1
        chip = "🔴"
        print(f"Here the chip {chip}")
        board[row][col] = chip
        create_board()


def select_mode_and_username():
    """
    Request to the user the mode(Single Player or Multiplayer)
    and ask for the Usernames
    """
    print("Are you ready for the Ultimate Connect 4 Battle?\n")
    select_mode = input("How many player?\n")
    if select_mode == "1":
        print("Wrong choise! This option is not available yet! Try again! \n")
        select_mode_and_username()
    elif select_mode == "2":
        player_one_name = input("Player 1 what's your name?\n")
        print(f"Hi {player_one_name}!\n")
        
        player_two_name = input("Player 2 what's your name?\n")
        print(f"Hi {player_two_name}!\n")
        
        print("Great! Are you ready?! Let me prepare the Board!")
        print("")
        insert_value_matrix(0, 0, "")
    else:
        print("This is not a valid option. The available option are: 1 or 2! Please try again!\n")
        select_mode_and_username()
    
    
def start_game():
    """
    Ask to the user if they want to Start Playing 
    or read the Instructions.
    """
    cprint("               Welcome to Connect 4\n", "red")
    selection = input("Do you want to [P]lay or read the [I]nstructions?\n").lower()
    if selection == "p":
        select_mode_and_username()
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
    start_game()


main()