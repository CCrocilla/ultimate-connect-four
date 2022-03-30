import os
import random
import numpy as np
from pprint import pprint 
from termcolor import cprint


BOARD_ROW = 6
BOARD_COL = 7
player_1 = ""
player_2 = ""
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
    pause_program = input("Press the [ENTER] key to return Home...")


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
    print("Board")
    for row in range(BOARD_ROW):
        cprint("\n-------------------------------------", "blue")
        for col in range(BOARD_COL):
            cell = board[row][col]
            if cell == "":
                cell = " "
            #print(f"| {row} - {col}" , end="")
            cprint(f"|  {cell}  ", "blue", end="")                
    cprint("\n-------------------------------------", "blue")
    print("")


def insert_move_player(row, col):
    """
    Function to insert value in the Matrix!
    """
    clear_console()
    x = "X"
    board[row][col] = x
    create_board()


def select_mode_and_username():
    """
    Request to the user the mode(Single Player or Multiplayer)
    and ask for the Usernames
    """
    print("Are you ready for the Ultimate Connect 4 Battle?\n")
    select_mode = input("How many player?\n")
    if select_mode == "1":
        print("Wrong choise! This option is not available yet!\n")
        select_mode_and_username()
    elif select_mode == "2":
        player_1 = input("Player 1 how can I call you?\n")
        print(f"Hi {player_1}!\n")
        
        player_2 = input("Player 2 what's your name?\n")
        print(f"Hi {player_2}!\n")
        
        print("Great! Are you ready?! Let me prepare the Board!")
        print("")
        insert_move_player(1, 2)
    else:
        print("This is not a valid option. Please try again!\n")
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