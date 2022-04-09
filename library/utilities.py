""" Import OS """
import os
from termcolor import colored


let_enter = colored("ENTER", 'cyan')


def pause():
    """ Pause until the user press Enter """
    message_pause_home = f"Press the [{let_enter}] key to return Home...\n"
    input(message_pause_home)


def pause_continue():
    """ Pause until the user press Enter """
    message_pause_continue = f"Press the [{let_enter}] key to continue...\n"
    input(message_pause_continue)


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
