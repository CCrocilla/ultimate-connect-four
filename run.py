import os
import random
import numpy as np
from termcolor import cprint


BOARD_ROW = 6
BOARD_COL = 7
player_1 = ""
player_2 = ""


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
    pause_programm = input("Press the [ENTER] key to go to Home Menu...")


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
    Display the Instructions
    """
    instruction_logo = open("assets/files/instructions-logo.txt")
    cprint(instruction_logo.read(), "red")
    instruction_logo.close()
    cprint("                   Instructions\n", "red")
    instruction_rules = open("assets/files/instructions-rules.txt")
    cprint(instruction_rules.read(), "red")
    instruction_rules.close()
    pause()
    clear_console()
    main()


def create_board():
    print("Board")
    exit()
      
    
def start_game():
    """
    Ask to the user if they want to Start Playing 
    or read the Instructions.
    """
    cprint("               Welcome to Connect 4\n", "red")
    selection = input("Do you want to [P]lay or read the [I]nstructions?\n").lower()
    if selection == "p":
        create_board()
    elif selection == "i":
        clear_console()
        instruction()
    else:
        print("Invalid Selection")
        main()
        

def main():
    logo()
    start_game()


main()