""" Imports """
import os
from termcolor import colored, cprint


def pause():
    """ Pause until the user press Enter """
    let_enter = colored("ENTER", 'cyan')
    message_pause_home = f"Press the [{let_enter}] key to return Home...\n"
    input(message_pause_home)


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


def display_logo():
    """ Display the ASCII Logo """
    with open("assets/files/logo.txt", encoding="utf-8") as logo:
        main_menu = logo.read()
        cprint(main_menu, "red")
