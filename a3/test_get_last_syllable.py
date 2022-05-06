"""CSCA08H1: Assignment 3: Poetry Form Checker

Instructions (READ THIS FIRST!)
===============================

Make sure that the code files:
    poetry_functions.py, poetry_program.py, poetry_reader.py,
    test_get_last_syllable.py,
    a3_checker.py, a3_pyta.json and checker_generic.py,
the folder dataset that includes files:
    pronunication_dictionary.txt, pronunication_dictionary_small.txt,
    poetry_forms.txt and poetry_forms_small.txt, and
the folder sample_poems that includes files:
    haiku1.txt, haiku2.txt, etc.
are in the same folder as this file (poetry_constants.py).

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the course CSC108/CSCA08 at the University of Toronto. Copying for
purposes other than this use is expressly prohibited. All forms of distribution
of this code, whether as given or with any changes, are expressly prohibited.

All of the files in this folder are:
Copyright (c) 2022 the University of Toronto CSC108/CSCA08 Teaching Team.
"""

import unittest
import poetry_functions


class TestGetLastSyllable(unittest.TestCase):

    def test_get_last_syllable_empty(self):
        """Test get_last_syllable on an empty tuple."""

        actual = poetry_functions.get_last_syllable(())
        expected = ()
        self.assertEqual(actual, expected, 'empty tuple')

    # Place your unittest method definitions after this line.

    def test_get_last_syllable_single_vowel(self):
        """Test get_last_syllable on a tuple containing a single vowel.
        """

        actual = poetry_functions.get_last_syllable(('AE1',))
        expected = ('AE1',)
        msg = " Expected to get the tuple ('AE1',) as there are no other" \
            + "phoneme after it"
        self.assertEqual(actual, expected, msg)

    def test_get_last_syllable_single_consonant(self):
        """Test get_last_syllable on a tuple containing a single consonant.
        """

        actual = poetry_functions.get_last_syllable(('B',))
        expected = ()
        msg = " Expected to get the tuple () as there are no vowel phoneme"
        self.assertEqual(actual, expected, msg)

    def test_get_last_syllable_no_vowels(self):
        """Test get_last_syllable on a tuple containing no vowels.
        """

        actual = poetry_functions.get_last_syllable(('B', 'S'))
        expected = ()
        msg = " Expected to get the tuple () as there are no vowel phonemes"
        self.assertEqual(actual, expected, msg)

    def test_get_last_syllable_only_vowels(self):
        """Test get_last_syllable on a tuple containing only vowels.
        """

        actual = poetry_functions.get_last_syllable(('EY2', 'EY1'))
        expected = ('EY1',)
        msg = " Expected to get the tuple ('EY1') as it is the last" \
            + "vowel phonemes and nothing after it"
        self.assertEqual(actual, expected, msg)

    def test_get_last_syllable_multiple_vowels(self):
        """Test get_last_syllable on a tuple containing multiple vowels.
        """

        actual = poetry_functions.get_last_syllable(('EH1', 'R', 'AH0', 'N'))
        expected = ('AH0', 'N')
        msg = " Expected to get the tuple ('AH0', 'N') as 'AH0' is " \
            + "last vowel phoneme and 'N' is after it"
        self.assertEqual(actual, expected, msg)

    def test_get_last_syllable_same_vowels(self):
        """Test get_last_syllable on a tuple containing same vowels.
        """

        actual = poetry_functions.get_last_syllable(('AA2', 'L', 'IY1', 'AA2'))
        expected = ('AA2',)
        msg = " Expected to get the tuple ('AA2',) as there are no other" \
            + "phonemes after it"
        self.assertEqual(actual, expected, msg)

    def test_get_last_syllable_only_starting_vowel(self):
        """Test get_last_syllable on a tuple starting with a no vowels after.
        """

        actual = poetry_functions.get_last_syllable(('AE1', 'B'))
        expected = ('AE1', 'B')
        msg = " Expected to get the tuple ('AE1', 'B') as 'B' is after the" \
            + "vowel phoneme 'AE1'"
        self.assertEqual(actual, expected, msg)

    def test_get_last_syllable_ending_vowel(self):
        """Test get_last_syllable on a tuple ending with a vowel.
        """

        actual = poetry_functions.get_last_syllable(('AE1', 'B', 'AH0'))
        expected = ('AH0',)
        msg = " Expected to get the tuple ('AH0',) as there are no other" \
            + "phonemes after it"
        self.assertEqual(actual, expected, msg)

    def test_get_last_syllable_non_endpoint_vowel(self):
        """Test get_last_syllable on a tuple with a vowel that is neither at \
        beginning or the end of the tuplple."""

        actual = poetry_functions.get_last_syllable(('B', 'AE1', 'G', 'Z'))
        expected = ('AE1', 'G', 'Z')
        msg = " Expected to get the tuple ('AE1', 'G', 'Z') as 'AE1' is the" \
            + "vowel phoneme and 'G', 'Z' are after it"
        self.assertEqual(actual, expected, msg)

# Place your unittest method definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
