""" Import termcolor in order to print with colors in Terminal """
from termcolor import cprint


def check_if_board_full(board):
    """
    Check if any of the string in the array is empty.
    If there is no empty string in the array then return
    True value and the game is over as tie
    """
    if any("" in element for element in board):
        return False
    else:
        cprint("Game Over! The Board is full! This is a tie!", "red")
        return True


def check_for_winner(board, name, coin, board_rows, board_cols):
    """ Check for the Horizontal/Vertical/Diagonal Winner """
    #Check for Horizontal Winner
    for col in range(4):
        for row in range(board_rows):
            if board[row][col] == board[row][col+1] == \
                board[row][col+2] == board[row][col+3] == coin:
                cprint(f"🎉 {name} you are the WINNER!!! Congratulations!!! 🎉", "yellow")
                return True

    # Check for Vertical Winner
    for col in range(board_cols):
        for row in range(3):
            if board[row][col] == board[row+1][col] == \
                board[row+2][col] == board[row+3][col] == coin:
                cprint(f"🎉 {name} you are the WINNER!!! Congratulations!!! 🎉", "yellow")
                return True

    #Check for Diagonal Winner
    for col in range(4):
        for row in range(3):
            if board[row][col] == board[row+1][col+1] == \
                board[row+2][col+2] == board[row+3][col+3] == coin:
                cprint(f"🎉 {name} you are the WINNER!!! Congratulations!!! 🎉", "yellow")
                return True

    #Check for Negative Diagonal Winner
    for col in range(4):
        for row in range(5, 2, -1):
            if board[row][col] == board[row-1][col+1] == \
                board[row-2][col+2] == board[row-3][col+3] == coin:
                cprint(f"🎉 {name} you are the WINNER!!! Congratulations!!! 🎉", "yellow")
                return True
            