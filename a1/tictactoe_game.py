"""CSCA08: Main program for the tic-tac-toe game.

Instructions (READ THIS FIRST!)
===============================

Make sure that the files tictactoe_functions.py and a1_checker.py are in the
same folder as this file (tictactoe_game.py).

DO NOT MAKE CHANGES TO THIS FILE.

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the course CSC108/CSCA08 at the University of Toronto. Copying for 
purposes other than this use is expressly prohibited. All forms of distribution 
of this code, whether as given or with any changes, are expressly prohibited.

All of the files in this folder are:
Copyright (c) 2022 the University of Toronto CSC108/CSCA08 Teaching Team.
"""


import random
from typing import Tuple
import tictactoe_functions

MAX_BOARD_SIZE = 9
SYMBOLS = 'OX'
COMPUTER = 0
HUMAN = 1


def is_valid_response(response: str, min_value: int, max_value: int) -> bool:
    """Return True if and only if the string response contains the
    representation of an int value without a +/- sign that is between min_value
    and max_value, inclusive.

    >>> is_valid_response('4', 1, 9)
    True
    >>> is_valid_response('4', 5, 9)
    False
    >>> is_valid_response('abc', 1, 3)
    False
    """

    return (response.isdigit()
            and tictactoe_functions.is_between(int(response),
                                               min_value - 1, max_value + 1))


def get_valid_response(prompt_message: str, error_message: str,
                       min_value: int, max_value: int) -> int:
    """Return the user's response to prompt_message, as an int, possibly after
    repeated prompting.  Display error_message when response is not the str
    representation of an int value without a +/- sign that is between min_value
    and max_value, inclusive.

    (No docstring example given since function depends on user input.)
    """

    response = input(prompt_message)
    while not is_valid_response(response, min_value, max_value):
        print(error_message)
        response = input(prompt_message)

    return int(response)


def get_game_size() -> int:
    """Return the valid tic-tac-toe game board size entered by game player.

    (No docstring example given since the function depends on user input.)
    """

    prompt_message = ('\nEnter desired game board size (an int between 1 and '
                      + str(MAX_BOARD_SIZE) + '): ')
    error_message = 'Your requested game board size is not valid.  Try again!'

    return get_valid_response(prompt_message, error_message, 1, MAX_BOARD_SIZE)


def is_occupied(row_index: int, col_index: int, game_board: str) -> int:
    """Return True if and only if the cell with indices row_index and col_index
    in the tic-tac-toe game_board does not contain the EMPTY_CELL character.

    Precondition: row_index and col_index are valid indices for a cell in the
                  tic-tac-toe game_board.

    >>> is_occupied(1, 1, 'XOX-')
    True
    >>> is_occupied(2, 2, 'XOX-')
    False
    """

    board_size = tictactoe_functions.get_board_size(game_board)
    position = tictactoe_functions.get_string_index(row_index, col_index,
                                                    board_size)
    return game_board[position] != tictactoe_functions.EMPTY_CELL


def get_row_col(is_human_move: bool, game_board: str) -> Tuple[int, int]:
    """Return an ordered pair of row and column indices that are valid for the
    tic-tac-toe game_board.  When is_human_move is True, player is prompted
    for indices, otherwise they are randomly generated.

    (No docstring example given since the function either depends on user
    input or randomly generated numbers.)
    """

    board_size = tictactoe_functions.get_board_size(game_board)
    if is_human_move:
        print('Your move.  Enter row and column numbers between 1 and '
              + str(board_size) + '.')
        row = get_valid_response('Enter row number: ',
                                 'Your suggested row number was invalid!',
                                 1, board_size)
        col = get_valid_response('Enter column number: ',
                                 'Your suggested column number was invalid!',
                                 1, board_size)
    else:
        row = random.randint(1, board_size)
        col = random.randint(1, board_size)

    return (row, col)


def get_move(is_human_move: bool, game_board: str) -> Tuple[int, int]:
    """Return player's move as an ordered pair of row and column indices that
    are valid for the tic-tac-toe game_board.

    (No docstring example given since the function indirectly depends on either
    user input or randomly generated numbers.)
    """

    (row, col) = get_row_col(is_human_move, game_board)
    while is_occupied(row, col, game_board):
        if is_human_move:
            print('That spot is already taken!  Try again.')
        (row, col) = get_row_col(is_human_move, game_board)

    return (row, col)

# Interested in why this docstring starts with an r?
# See section 2.4.1:
# https://docs.python.org/3.10/reference/lexical_analysis.html


def format_game_board(game_board: str) -> str:
    """Format the tic-tac-toe game_board in a nice grid format for printing.

    >>> format_game_board('XOX-')
    "\nThe X's and O's board:\n\n   1   2  \n\n1  X | O\n  ---+---\n2  X | -\n"
    """

    board_size = tictactoe_functions.get_board_size(game_board)

    formatted_board = ''
    # Format the title.
    formatted_board += '\nThe X\'s and O\'s board:\n\n'

    # Add in the column numbers.
    formatted_board += '  '
    for col in range(1, board_size):
        formatted_board += (' ' + str(col) + '  ')
    formatted_board += (' ' + str(board_size) + '  \n\n')

    # Add in the row numbers, board contents and grid markers.
    position = 0
    for row in range(1, board_size + 1):
        formatted_board += (str(row) + ' ')
        for col in range(1, board_size):
            formatted_board += (' ' + game_board[position] + ' |')
            position = position + 1
        formatted_board += (' ' + game_board[position] + '\n')
        position = position + 1
        if row < board_size:
            formatted_board += ('  ' + '---+' * (board_size - 1) + '---\n')

    return formatted_board


def game_won(game_board: str, symbol: str) -> bool:
    """Return True if and only if the player using symbol has won the
    tic-tac-toe game represented by game_board.

    >>> game_won('XXX-O-O--', 'X')
    True
    >>> game_won('XOXOXOOXO', 'X')
    False
    """

    board_size = tictactoe_functions.get_board_size(game_board)
    winning_string = symbol * board_size

    for col in range(1, board_size + 1):
        extract = tictactoe_functions.get_line(game_board, 'down', col)
        if extract == winning_string:
            return True

    for row in range(1, board_size + 1):
        extract = tictactoe_functions.get_line(game_board, 'across', row)
        if extract == winning_string:
            return True

    extract = tictactoe_functions.get_line(game_board, 'down_diagonal', 1)
    if extract == winning_string:
        return True

    extract = tictactoe_functions.get_line(game_board, 'up_diagonal', 1)
    if extract == winning_string:
        return True

    return False


def play_tictactoe() -> None:
    """Play a single game of tic-tac-toe, with one player being the program
    user and the other player being this computer program.

    (No docstring example given since the function indirectly depends on either
    user input or randomly generated numbers.)
    """

    # Initialize the game setup.
    board_size = get_game_size()
    game_board = tictactoe_functions.make_new_board(board_size)

    print('\nYou are using symbol ' + SYMBOLS[HUMAN] + ' and the computer '
          + 'program is using symbol ' + SYMBOLS[COMPUTER] + '.')
    print(format_game_board(game_board))

    # Play the game until a player wins or there is a draw.
    is_human_move = False
    have_a_winner = False
    while (not have_a_winner
           and not tictactoe_functions.game_board_full(game_board)):

        is_human_move = not is_human_move
        (row, col) = get_move(is_human_move, game_board)
        if is_human_move:
            player_symbol = SYMBOLS[HUMAN]
            print('\nYou chose row ' + str(row) + ' and column '
                  + str(col) + '.')
        else:
            player_symbol = SYMBOLS[COMPUTER]
            print('The computer program then chose row ' + str(row)
                  + ' and column ' + str(col) + '.')

        game_board = tictactoe_functions.change_cell(
            player_symbol, row, col, game_board)

        if not is_human_move:
            print(format_game_board(game_board))

        have_a_winner = game_won(game_board, player_symbol)

    if have_a_winner:
        print('We have a winner!')
        if is_human_move:
            print(format_game_board(game_board))
            print('You beat the computer program! Congratulations!')
        else:
            print('The computer program won!')
            print('Re-think your strategy and try again.')
    else:
        print(format_game_board(game_board))
        print('The game has played to a draw.')
        print('Re-think your strategy and try again.')


if __name__ == '__main__':

    play_tictactoe()
