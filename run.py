import random
import termcolor


def welcome_message():
    """
    Display the ASCII Logo
    """
    logo = open("assets/logo.txt")
    print(logo.read())
    logo.close()


welcome_message()


