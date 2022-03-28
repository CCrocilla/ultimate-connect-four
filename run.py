import random
from termcolor import colored, cprint


def logo():
    """
    Display the ASCII Logo
    """
    logo = open("assets/logo.txt")
    cprint(logo.read(), "red")
    logo.close()


def start_game():
    """
    Ask to the user if they want to Start Play 
    or read the Instruction.
    """
    cprint("               Welcome to Connect 4\n", "red")
    selection = input("Do you want to [P]lay or read the [I]nstructions?\n").lower()
    if selection == "p":
        print("Play!")
    elif selection == "i":
        print("Instruction")
    else:
        print("Invalid Selection")
        

def main():
    logo()
    start_game()


main()
