""" Import OS """
import os

def pause():
    """ Pause until the user press Enter """
    input("Press the [ENTER] key to return Home...\n")


def pause_continue():
    """ Pause until the user press Enter """
    input("Press the [ENTER] key to continue...\n")


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
