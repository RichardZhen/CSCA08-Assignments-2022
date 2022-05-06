"""CSCA08: Functions for the tic-tac-toe game.

Instructions (READ THIS FIRST!)
===============================

Make sure that the files tictactoe_game.py and a1_checker.py are in the same
folder as this file (tictactoe_functions.py).

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the course CSC108/CSCA08 at the University of Toronto. Copying for
purposes other than this use is expressly prohibited. All forms of distribution
of this code, whether as given or with any changes, are expressly prohibited.

All of the files in this folder are:
Copyright (c) 2022 the University of Toronto CSC108/CSCA08 Teaching Team.
"""


EMPTY_CELL = '-'


def is_between(value: int, min_value: int, max_value: int) -> bool:

    """Return True if and only if value is between min_value and max_value.

    Precondition: min_value < max_value

    >>> is_between(1, 0, 2)
    True
    >>> is_between(0, 2, 3)
    False
    >>> is_between(1, 1, 3)
    False
    """
    # Requires it to be an open interval between min_value and max_value

    return min_value < value < max_value


def game_board_full(game_board: str) -> bool:
    """ Return True if and only if there are no empty cells on the board

    >>> game_board_full('XOXOOXOXO')
    True
    >>> game_board_full('X-OX')
    False
    >>> game_board_full('')
    False
    """

    return EMPTY_CELL not in game_board and game_board not in ''


def get_board_size(game_board: str) -> int:
    """ Return the size of the board

    >>> get_board_size('XOXO')
    2
    >>> get_board_size('X-OX-XX-O')
    3
    >>> get_board_size('X')
    1
    """

    # Convert it to int or else it will return a float
    size_of_board = int((len(game_board))**(0.5))
    return size_of_board


def make_new_board(board_size: int) -> str:
    """ Return a new board that is string that contains empty cells in all
        the string indices

    >>> make_new_board(4)
    '----------------'
    >>> make_new_board(1)
    '-'
    >>> make_new_board(7)
    '-------------------------------------------------'
    """

    reset = EMPTY_CELL * (board_size)**2
    return reset


def get_string_index(row_index: int, col_index: int, board_size: int) -> int:
    """ Return the position of symbol based on the size of board as a
    number corresponding to the string index

    >>> get_string_index(2, 2, 4)
    5
    >>> get_string_index(3, 3, 9)
    20
    >>> get_string_index(1, 1, 1)
    0
    """

    # Example given
    string_index = (row_index - 1) * board_size + (col_index - 1)
    return string_index


def change_cell(player_symbol: str, row_index: int, col_index: int,
                board: str) -> str:
    """ Return a new board that replaces the empty cell with either symbol

    >>> change_cell('X', 1, 1, '-')
    'X'
    >>> change_cell('X', 2, 3, '---------')
    '-----X---'
    >>> change_cell('X', 2, 2, '----')
    '---X'
    """

    # get_string_index and get_board_size as helper functions to obtain
    # the size of the board and the position of the index
    size = get_board_size(board)
    position = get_string_index(row_index, col_index, size)
    # board[position + 1:] is to not overlap with the symbol that
    # player_symbol is replacing
    new_game_board = board[:position] + player_symbol + board[position + 1:]
    return new_game_board


def get_line(game_board: str, direction: str, place: int) -> str:
    """ Return the winning string based on the direction and the place
        (if needed)

    >>> get_line('XOXO', 'down', 1)
    'XX'
    >>> get_line('XOXXXXOXO', 'across', 2)
    'XXX'
    >>> get_line('X--OXXO-X', 'down_diagonal', 1)
    'XXX'
    >>> get_line('O-X-XOX--', 'up_diagonal', 1)
    'XXX'
    """

    size = get_board_size(game_board)
    if direction == 'down':
        win_con1 = game_board[place - 1::size]
        return win_con1
    elif direction == 'across':
        win_con2 = game_board[(place - 1) * size:place * size]
        return win_con2
    elif direction == 'down_diagonal':
        win_con3 = game_board[::size + 1]
        return win_con3
    elif direction == 'up_diagonal':
        win_con4 = game_board[size - 1:size * size - 1: size - 1]
        return win_con4
    else:
        return None
