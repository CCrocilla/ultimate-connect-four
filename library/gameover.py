""" Imports """
from termcolor import cprint
from library.utilities import clear_console


def check_if_board_full(board):
    """
    Check if any of the string in the array is empty.
    If there is no empty string in the array then return
    True value and the game is over as tie
    """
    if any("" in element for element in board):
        return False
    else:
        clear_console()
        cprint("Game Over! The Board is full! This is a tie!", "red")
        return True


def check_horizontal_winner(board, name, coin, board_rows):
    """ Check for the Horizontal Winner """
    for col in range(4):
        for row in range(board_rows):
            if board[row][col] == board[row][col+1] == \
               board[row][col+2] == board[row][col+3] == coin:
                clear_console()
                cprint(f"🎉  {name} you are the WINNER!!!" +
                       " Congratulations!!!  🎉", "yellow")
                return True


def check_vertical_winner(board, name, coin, board_cols):
    """ Check for the Vertical Winner """
    for col in range(board_cols):
        for row in range(3):
            if board[row][col] == board[row+1][col] == \
               board[row+2][col] == board[row+3][col] == coin:
                clear_console()
                cprint(f"🎉  {name} you are the WINNER!!!" +
                       " Congratulations!!!  🎉", "yellow")
                return True


def check_diagonal_winner(board, name, coin):
    """ Check for the Diagonal Winner """
    for col in range(4):
        for row in range(3):
            if board[row][col] == board[row+1][col+1] == \
                board[row+2][col+2] == board[row+3][col+3] == coin:
                clear_console()
                cprint(f"🎉  {name} you are the WINNER!!!" +
                       " Congratulations!!!  🎉", "yellow")
                return True

    #Check for Negative Diagonal Winner
    for col in range(4):
        for row in range(5, 2, -1):
            if board[row][col] == board[row-1][col+1] == \
                board[row-2][col+2] == board[row-3][col+3] == coin:
                clear_console()
                cprint(f"🎉  {name} you are the WINNER!!!" +
                       " Congratulations!!!  🎉", "yellow")
                return True
