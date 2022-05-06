"""CSCA08: Winter 2022 -- Assignment 1: Tic-Tac-Toe

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

from typing import Any, Dict
import unittest
import checker_generic
import tictactoe_functions as tf

PYTA_CONFIG = 'a1_pyta.json'
FILENAME = 'tictactoe_functions.py'
TARGET_LEN = 79
SEP = '='

CONSTANTS = {'EMPTY_CELL': '-'}


class CheckTest(unittest.TestCase):
    """Sanity checker for assignment functions."""

    def test_is_between(self) -> None:
        """Function is_between."""
        self._check(tf.is_between, [1, 0, 2], bool)

    def test_game_board_full(self) -> None:
        """Function game_board_full."""
        self._check(tf.game_board_full, ['XOOOXOOXX'], bool)

    def test_get_board_size(self) -> None:
        """Function get_board_size."""
        self._check(tf.get_board_size, [''], int)

    def test_make_new_board(self) -> None:
        """Function make_new_board."""
        self._check(tf.make_new_board, [1], str)

    def test_get_string_index(self) -> None:
        """Function get_string_index."""
        self._check(tf.get_string_index, [1, 1, 3], int)

    def test_change_cell(self) -> None:
        """Function change_cell."""
        self._check(tf.change_cell, ['X', 2, 1, '----'], str)

    def test_get_line(self) -> None:
        """Function get_line."""
        self._check(tf.get_line, ['XOXOXO--X', 'down', 2], str)

    def test_check_constants(self) -> None:
        """Values of constants."""

        print('\nChecking that constants refer to their original values')
        self._check_constants(CONSTANTS, tf)
        print('  check complete')

    def _check(self, func: callable, args: list, ret_type: type) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.

        """

        print('\nChecking {}...'.format(func.__name__))
        result = checker_generic.check(func, args, ret_type)
        self.assertTrue(result[0], result[1])
        print('  check complete')

    def _check_constants(self, name2value: Dict[str, object], mod: Any) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in name2value.items():
            actual = getattr(mod, name)
            msg = 'The value of constant {} should be {} but is {}.'.format(
                name, expected, actual)
            self.assertEqual(expected, actual, msg)


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(' End checking coding style '.center(TARGET_LEN, SEP))

print(' Start: checking type contracts '.center(TARGET_LEN, SEP))
unittest.main(exit=False)
print(' End checking type contracts '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style')
print('  - checking type contract\n')
