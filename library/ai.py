""" Functions to realize the IA of the CPU """

def check_move_horizontal(coin, coin_enemy, board, board_rows):
    """ Check possible horizontal move"""
    for col in range(4):
        for row in range(board_rows):
            positions = (0, 0)
            counter_coin_enemy = 0
            counter_coin = 0
            counter_empty = 0
            for shift in range(4):
                if board[row][col + shift] == coin_enemy:
                    counter_coin_enemy += 1
                if board[row][col + shift] == coin:
                    counter_coin += 1
                if board[row][col + shift] == "":
                    counter_empty += 1
                    positions = (row, col + shift)
            gravity_row = get_row_insert(board, board_rows, col + shift)
            if counter_coin + counter_empty == 4 and counter_coin >= 3:
                if gravity_row == positions[0]:
                    return positions

            if counter_coin_enemy + counter_empty == 4 and counter_coin_enemy >= 3:
                if gravity_row == positions[0]:
                    return positions
    return None


def check_move_vertical(coin, coin_enemy, board, board_cols):
    """ Check possible vertical move"""
    for col in range(board_cols):
        for row in range(3):
            positions = (0, 0)
            counter_coin_enemy = 0
            counter_coin = 0
            counter_empty = 0
            for shift in range(4):
                if board[row + shift][col] == coin_enemy:
                    counter_coin_enemy += 1
                if board[row + shift][col] == coin:
                    counter_coin += 1
                if board[row + shift][col] == "":
                    counter_empty += 1
                    positions = (row + shift, col)
            if counter_coin + counter_empty == 4 and counter_coin >= 3:
                return positions
            if counter_coin_enemy + counter_empty == 4 and counter_coin_enemy >= 3:
                return positions
    return None


def get_row_insert(board, board_rows, col):
    """ Function to realize the gravity for the Coins """
    row_ins = -1
    for row in range(board_rows):
        cell = board[board_rows - row - 1][col]
        if cell == "":
            row_ins = board_rows - row - 1
            break
    return row_ins
