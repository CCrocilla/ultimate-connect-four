""" Functions to realize the AI of the CPU """


def check_move_horizontal(coin, coin_enemy, board, board_rows):
    """ Check possible horizontal move"""
    for col in range(4):
        for row in range(board_rows):
            positions = (0, 0)
            count_coin_enemy = 0
            count_coin = 0
            count_empty = 0
            for shift in range(4):
                if board[row][col + shift] == coin_enemy:
                    count_coin_enemy += 1
                if board[row][col + shift] == coin:
                    count_coin += 1
                if board[row][col + shift] == "":
                    count_empty += 1
                    positions = (row, col + shift)
            gravity_row = get_row_insert(board, board_rows, col + shift)
            if count_coin + count_empty == 4 and count_coin >= 2:
                if gravity_row == positions[0]:
                    return positions

            if count_coin_enemy + count_empty == 4 and count_coin_enemy >= 2:
                if gravity_row == positions[0]:
                    return positions
    return None


def check_move_vertical(coin, coin_enemy, board, board_cols):
    """ Check possible vertical move"""
    for col in range(board_cols):
        for row in range(3):
            positions = (0, 0)
            count_coin_enemy = 0
            count_coin = 0
            count_empty = 0
            for shift in range(4):
                if board[row + shift][col] == coin_enemy:
                    count_coin_enemy += 1
                if board[row + shift][col] == coin:
                    count_coin += 1
                if board[row + shift][col] == "":
                    count_empty += 1
                    positions = (row + shift, col)
            if count_coin + count_empty == 4 and count_coin >= 2:
                return positions
            if count_coin_enemy + count_empty == 4 and count_coin_enemy >= 2:
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
