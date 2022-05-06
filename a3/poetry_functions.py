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

from typing import List, Tuple, Dict

from poetry_constants import (POEM_LINE, POEM, PHONEMES, PRONUNCIATION_DICT,
                              POETRY_FORM_DESCRIPTION)

# ===================== Provided Helper Functions =====================


def transform_string(s: str) -> str:
    """Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> transform_string('Birthday!!!')
    'BIRTHDAY'
    >>> transform_string('"Quoted?"')
    'QUOTED'
    >>> transform_string('To be? Or not to be?')
    'TO BE? OR NOT TO BE'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


def is_vowel_phoneme(phoneme: str) -> bool:
    """Return True if and only if phoneme is a vowel phoneme. That is, whether
    phoneme ends in a 0, 1, or 2.

    Precondition: len(phoneme) > 0 and phoneme.isupper()

    >>> is_vowel_phoneme('AE0')
    True
    >>> is_vowel_phoneme('DH')
    False
    >>> is_vowel_phoneme('IH2')
    True
    """

    return phoneme[-1] in '012'


# ===================== Add Your Helper Functions Here =====================

def remove_inner_punctuation(x: str) -> str:
    """ Returns a new string based on x that removes the punctuation if the
    word starts or end with punctuation
    >>> remove_inner_punctuation("That rains 'till I'm covered with slime.")
    "THAT RAINS TILL I'M COVERED WITH SLIME"
    >>> remove_inner_punctuation('We are the Dead. Short days ago')
    'WE ARE THE DEAD SHORT DAYS AGO'
    >>> remove_inner_punctuation('To be? Or not to be?')
    'TO BE OR NOT TO BE'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    res = ""
    phrase = transform_string(x).split()
    for word in phrase:
        if word[0] in punctuation or word[-1] in punctuation:
            word = transform_string(word)
        res += word + " "
    res = res[:len(res) - 1]
    return res


def string_to_phonemes(x: str, word_to_phonemes: PRONUNCIATION_DICT) -> \
                        PHONEMES:
    """ Convert the given string x into a phoneme based on
    word_to_phonemes

    >>> string_to_phonemes('thine', word_to_phonemes)
    ('DH', 'AY1', 'N')
    >>> string_to_phonemes('devine', word_to_phonemes)
    ('D', 'AH0', 'V', 'AY1', 'N')
    >>> string_to_phonemes('heard', word_to_phonemes)
    ('HH', 'ER1', 'D')
    """

    word = x.upper()
    res = ()
    if word in word_to_phonemes:
        res = word_to_phonemes[word]
    return res


def string_into_tuple(filler: str) -> tuple:
    """ Converts filler into a tuple without spliting it

        Precondition: len(filler) > 0

    >>> string_into_tuple('AH0')
    ('AH0',)
    >>> string_into_tuple('AY1')
    ('AY1',)
    """

    tpl = ()
    if type(filler) is str:
        tpl += (filler,)
    return tpl


def unique_items(rhyme_scheme: Tuple[str]) -> list:
    """ Returns a list of items that are the unique items in rhyme_scheme
    >>> unique_items(('A', 'A', 'B', 'B', 'A'))
    ['A', 'B']
    >>> unique_items(('*', '*', '*', '*', '*'))
    ['*']
    """
    unique = []
    for i in rhyme_scheme:
        if i not in unique:
            unique += i
    return unique


def list_of_indices(obj: str, rhyme_scheme: Tuple[str]) -> list:
    """ Returns the list of indices where obj occurs in rhyme_scheme
    >>> list_of_indices('A',('A', 'A', 'B', 'B', 'A'))
    [0, 1, 4]
    >>> list_of_indices('B',('A', 'A', 'B', 'B', 'A'))
    [2, 3]
    >>> list_of_indices('*', ('*', '*', '*', '*', '*'))
    [0, 1, 2, 3, 4]
    """

    lst = []
    count = 0
    uniques = unique_items(rhyme_scheme)
    for item in uniques:
        if obj == item:
            for char in rhyme_scheme:
                if obj == char:
                    lst.append(rhyme_scheme.index(char, count))
                    count = (rhyme_scheme.index(char, count) + 1)
    return lst


def line_to_phonemes(poem_lines: POEM,
                     words_to_phonemes: PRONUNCIATION_DICT) -> \
                        List[List[PHONEMES]]:
    """ Converts the poem_lines based on words_to_phonemes into syllable form
    >>> poem_lines = ['The first line leads off,',
    ...               'With a gap before the next.', 'Then the poem ends.']
    >>> word_to_phonemes = {'NEXT': ('N', 'EH1', 'K', 'S', 'T'),
    ...                     'GAP': ('G', 'AE1', 'P'),
    ...                     'BEFORE': ('B', 'IH0', 'F', 'AO1', 'R'),
    ...                     'LEADS': ('L', 'IY1', 'D', 'Z'),
    ...                     'WITH': ('W', 'IH1', 'DH'),
    ...                     'LINE': ('L', 'AY1', 'N'),
    ...                     'THEN': ('DH', 'EH1', 'N'),
    ...                     'THE': ('DH', 'AH0'),
    ...                     'A': ('AH0'),
    ...                     'FIRST': ('F', 'ER1', 'S', 'T'),
    ...                     'ENDS': ('EH1', 'N', 'D', 'Z'),
    ...                     'POEM': ('P', 'OW1', 'AH0', 'M'),
    ...                     'OFF': ('AO1', 'F')}
    >>> line_to_phonemes(poem_lines, word_to_phonemes)
    ...                    [[('DH', 'AH0'),
    ...                     ('F', 'ER1', 'S', 'T'),
    ...                     ('L', 'AY1', 'N'),
    ...                     ('L', 'IY1', 'D', 'Z'),
    ...                     ('AO1', 'F')],
    ...                     [('W', 'IH1', 'DH'),
    ...                     'AH0',
    ...                     ('G', 'AE1', 'P'),
    ...                     ('B', 'IH0', 'F', 'AO1', 'R'),
    ...                     ('DH', 'AH0'),
    ...                     ('N', 'EH1', 'K', 'S', 'T')],
    ...                     [('DH', 'EH1', 'N'),
    ...                     ('DH', 'AH0'),
    ...                     ('P', 'OW1', 'AH0', 'M'),
    ...                     ('EH1', 'N', 'D', 'Z')]]
    """

    lst = []
    for lines in poem_lines:
        a = remove_inner_punctuation(lines).split()
        lst.append(a)
    for word in lst:
        for i in range(len(word)):
            if word[i] in words_to_phonemes:
                word[i] = words_to_phonemes[word[i]]
    return lst


def phoneme_concat(pho_lines: List[List]) -> List[Tuple]:
    """ Return a list of tuples that concatenates tuples in the inner list
    in pho_lines
    >>> pho_lines = [[('DH', 'AH0'),
    ...               ('F', 'ER1', 'S', 'T'),
    ...               ('L', 'AY1', 'N'),
    ...               ('L', 'IY1', 'D', 'Z'),
    ...               ('AO1', 'F')],
    ...               [('W', 'IH1', 'DH'),
    ...                 'AH0',
    ...                ('G', 'AE1', 'P'),
    ...                ('B', 'IH0', 'F', 'AO1', 'R'),
    ...                ('DH', 'AH0'),
    ...                ('N', 'EH1', 'K', 'S', 'T')],
    ...               [('DH', 'EH1', 'N'),
    ...                ('DH', 'AH0'),
    ...                ('P', 'OW1', 'AH0', 'M'),
    ...                ('EH1', 'N', 'D', 'Z')]]
    >>> phoneme_concat(pho_lines)
    [('DH', 'AH0', 'F', 'ER1', 'S', 'T', 'L', 'AY1', 'N', 'L', 'IY1', 'D', \
    'Z', 'AO1', 'F'),('W', 'IH1', 'DH', 'AH0', 'G', 'AE1', 'P', 'B', 'IH0', \
    'F', 'AO1', 'R', 'DH', 'AH0', 'N', 'EH1', 'K', 'S', 'T'),('DH', 'EH1', \
    'N', 'DH', 'AH0', 'P', 'OW1', 'AH0', 'M', 'EH1', 'N', 'D', 'Z')]
    """

    elst = []
    for item in pho_lines:
        for i in range(len(item)):
            if type(item[i]) is str:
                item[i] = string_into_tuple(item[i])
    for pho in pho_lines:
        a = sum(pho, ())
        elst.append(a)
    return elst


def correct_syllable_count(poem_lines: POEM,
                           description: POETRY_FORM_DESCRIPTION,
                           word_to_phonemes: PRONUNCIATION_DICT) -> \
                           List[POEM_LINE]:
    """Return a list of lines from poem_lines that do have the right
    number of syllables as specified by the poetry form description, according
    to the pronunciation dictionary word_to_phonemes. If all lines do not
    have the right number of syllables, return the empty list.

    Precondition: len(poem_lines) == len(description[0])

    >>> poem_lines = ['The first line leads off,',
    ...               'With a gap before the next.', 'Then the poem ends.']
    >>> description = ((5, 5, 4), ('*', '*', '*'))
    >>> word_to_phonemes = {'NEXT': ('N', 'EH1', 'K', 'S', 'T'),
    ...                     'GAP': ('G', 'AE1', 'P'),
    ...                     'BEFORE': ('B', 'IH0', 'F', 'AO1', 'R'),
    ...                     'LEADS': ('L', 'IY1', 'D', 'Z'),
    ...                     'WITH': ('W', 'IH1', 'DH'),
    ...                     'LINE': ('L', 'AY1', 'N'),
    ...                     'THEN': ('DH', 'EH1', 'N'),
    ...                     'THE': ('DH', 'AH0'),
    ...                     'A': ('AH0'),
    ...                     'FIRST': ('F', 'ER1', 'S', 'T'),
    ...                     'ENDS': ('EH1', 'N', 'D', 'Z'),
    ...                     'POEM': ('P', 'OW1', 'AH0', 'M'),
    ...                     'OFF': ('AO1', 'F')}
    >>> correct_syllable_count(poem_lines, description, word_to_phonemes)
    ['The first line leads off,']
    >>> poem_lines = ['The first line leads off,']
    >>> description = ((0,), ('*'))
    >>> correct_syllable_count(poem_lines, description, word_to_phonemes)
    ['The first line leads off,']
    """

    blank = []
    elst = []
    req_syllables = description[0]
    for i in poem_lines:
        a = get_syllable_count(i, word_to_phonemes)
        blank.append(a)
    for j in range(0, len(req_syllables)):
        if blank[j] == req_syllables[j] or req_syllables[j] == 0:
            elst.append(poem_lines[j])
    return elst


def subject_to_change(index: List[int], poem_lines: POEM) -> POEM:
    """

    Precondition: The max(index) <= len(poem_lines) - 1

    >>> index = [0, 2]
    >>> poem_lines = ['The first line leads off,',
    ... 'With a gap before the next.', Then the poem ends.',
    ... 'Leads off before.']
    >>> subject_to_change(index, poem_lines)
    ['The first line leads off,', 'Then the poem ends.']
    """

    blank = []
    for item in index:
        blank.append(poem_lines[item])
    return blank


def only_stars(star: str, rhyme_pattern: Tuple[str]) -> bool:
    """ Returns True only if rhyme_pattern only contains star
    >>> star = '*'
    >>> rhyme_pattern = ('*', '*', '*')
    >>> only_stars(star, rhyme_pattern)
    True
    >>> rhyme_pattern = ('A', '*', '*')
    >>> only_stars(star, rhyme_pattern)
    False
    >>> rhyme_pattern = ('*', 'A', '*')
    >>> only_stars(star, rhyme_pattern)
    False
    >>> rhyme_pattern = ('*', '*', 'A')
    >>> only_stars(star, rhyme_pattern)
    False
    """

    T = True
    for char in rhyme_pattern:
        if char == star:
            T = True
        else:
            T = False
            return T
    return T

# ===================== Required Functions =================================


# Functions related to syllable counts


def get_syllable_count(poem_line: POEM_LINE,
                       words_to_phonemes: PRONUNCIATION_DICT) -> int:
    """Return the number of syllables in poem_line by using the pronunciation
    dictionary words_to_phonemes.

    Precondition: len(poem_line) > 0

    >>> line = 'Then! the #poem ends.'
    >>> word_to_phonemes = {'THEN': ('DH', 'EH1', 'N'),
    ...                     'ENDS': ('EH1', 'N', 'D', 'Z'),
    ...                     'THE': ('DH', 'AH0'),
    ...                     'POEM': ('P', 'OW1', 'AH0', 'M')}
    >>> get_syllable_count(line, word_to_phonemes)
    5
    """

    num_syllable = 0
    split_line = (remove_inner_punctuation(poem_line)).split()
    for word in split_line:
        if word in words_to_phonemes:
            for key in words_to_phonemes[word]:
                if is_vowel_phoneme(key) is True:
                    num_syllable += 1
    return num_syllable


def check_syllable_counts(poem_lines: POEM,
                          description: POETRY_FORM_DESCRIPTION,
                          word_to_phonemes: PRONUNCIATION_DICT) \
        -> List[POEM_LINE]:
    """Return a list of lines from poem_lines that do NOT have the right
    number of syllables as specified by the poetry form description, according
    to the pronunciation dictionary word_to_phonemes.  If all lines have the
    right number of syllables, return the empty list.

    Precondition: len(poem_lines) == len(description[0])

    >>> poem_lines = ['The first line leads off,',
    ...               'With a gap before the next.', 'Then the poem ends.']
    >>> description = ((5, 5, 4), ('*', '*', '*'))
    >>> word_to_phonemes = {'NEXT': ('N', 'EH1', 'K', 'S', 'T'),
    ...                     'GAP': ('G', 'AE1', 'P'),
    ...                     'BEFORE': ('B', 'IH0', 'F', 'AO1', 'R'),
    ...                     'LEADS': ('L', 'IY1', 'D', 'Z'),
    ...                     'WITH': ('W', 'IH1', 'DH'),
    ...                     'LINE': ('L', 'AY1', 'N'),
    ...                     'THEN': ('DH', 'EH1', 'N'),
    ...                     'THE': ('DH', 'AH0'),
    ...                     'A': ('AH0'),
    ...                     'FIRST': ('F', 'ER1', 'S', 'T'),
    ...                     'ENDS': ('EH1', 'N', 'D', 'Z'),
    ...                     'POEM': ('P', 'OW1', 'AH0', 'M'),
    ...                     'OFF': ('AO1', 'F')}
    >>> check_syllable_counts(poem_lines, description, word_to_phonemes)
    ['With a gap before the next.', 'Then the poem ends.']
    >>> poem_lines = ['The first line leads off,']
    >>> description = ((0,), ('*'))
    >>> check_syllable_counts(poem_lines, description, word_to_phonemes)
    []
    """

    blank = []
    elst = []
    syllable_num = description[0]
    for i in poem_lines:
        a = get_syllable_count(i, word_to_phonemes)
        blank.append(a)
    for j in range(len(syllable_num)):
        if blank[j] != syllable_num[j] and syllable_num[j] != 0:
            elst.append(poem_lines[j])
    return elst


# Functions related to rhyming


def get_last_syllable(word_phonemes: PHONEMES) -> PHONEMES:
    """Return the last syllable from word_phonemes.

    The last syllable in word_phonemes is formed from the last vowel phoneme
    and any subsequent consonant phoneme(s) in word_phonemes, in the same
    order as they appear in word_phonemes.

    >>> get_last_syllable(('AE1', 'B', 'S', 'IH0', 'N', 'TH'))
    ('IH0', 'N', 'TH')
    >>> get_last_syllable(('IH0', 'N'))
    ('IH0', 'N')
    >>> get_last_syllable(('B', 'S'))
    ()
    """

    last = ()
    c = 0
    for syllable in word_phonemes:
        if is_vowel_phoneme(syllable) is True:
            last += (syllable,)
    for v in last:
        if last.index(v, c) == (len(last) - 1):
            last = word_phonemes[word_phonemes.index(v, c):
                                 len(word_phonemes) + 1]
            return last
        c = (last.index(v, c) + 1)
    return last


def words_rhyme(word1: str, word2: str, word_to_phonemes: PRONUNCIATION_DICT) \
        -> bool:
    """Return True if and only if word1 and word2 rhyme according to
    word_to_phonemes.

    Recall that two words rhyme if and only if they have the same last
    syllable.

    >>> word_to_phonemes = {'THINE': ('DH', 'AY1', 'N'),
    ...                     'DEVINE': ('D', 'AH0', 'V', 'AY1', 'N'),
    ...                     'HEARD': ('HH', 'ER1', 'D')}
    >>> words_rhyme('thine', 'devine', word_to_phonemes)
    True
    >>> words_rhyme('thine', 'heard', word_to_phonemes)
    False
    """

    term1 = string_to_phonemes(word1, word_to_phonemes)
    term2 = string_to_phonemes(word2, word_to_phonemes)
    if term1[-1] == term2[-1]:
        return True
    else:
        return False


def all_lines_rhyme(poem_lines: POEM, lines_to_check: List[int],
                    word_to_phonemes: PRONUNCIATION_DICT) -> bool:
    """Return True if and only if the lines from poem_lines with index in
    lines_to_check all rhyme, according to word_to_phonemes.

    Precondition: lines_to_check != []

    >>> poem_lines = ['The mouse', 'in my house', 'electric.']
    >>> lines_to_check = [0, 1]
    >>> word_to_phonemes = {'THE': ('DH', 'AH0'),
    ...                     'MOUSE': ('M', 'AW1', 'S'),
    ...                     'IN': ('IH0', 'N'),
    ...                     'MY': ('M', 'AY1'),
    ...                     'HOUSE': ('HH', 'AW1', 'S'),
    ...                     'ELECTRIC': ('IH0', 'L', 'EH1', 'K',
    ...                                  'T', 'R', 'IH0', 'K')}
    >>> all_lines_rhyme(poem_lines, lines_to_check, word_to_phonemes)
    True
    >>> lines_to_check = [0, 1, 2]
    >>> all_lines_rhyme(poem_lines, lines_to_check, word_to_phonemes)
    False
    >>> lines_to_check = [2]
    >>> all_lines_rhyme(poem_lines, lines_to_check, word_to_phonemes)
    True
    """

    rhyme_lst = []
    does_it_rhyme = False
    faker = line_to_phonemes(poem_lines, word_to_phonemes)
    noob = phoneme_concat(faker)
    for j in lines_to_check:
        rhyme_lst.append(noob[j][-1])
    for pho in rhyme_lst:
        if rhyme_lst[0] == pho:
            does_it_rhyme = True
        else:
            does_it_rhyme = False
            return does_it_rhyme
    return does_it_rhyme


def get_symbol_to_lines(rhyme_scheme: Tuple[str]) -> Dict[str, List[int]]:
    """Return a dictionary where each key is an item in rhyme_scheme and
    its corresponding value is a list of the indexes in rhyme_scheme where
    the item appears.

    >>> result = get_symbol_to_lines(('A', 'A', 'B', 'B', 'A'))
    >>> expected = {'A': [0, 1, 4], 'B': [2, 3]}
    >>> expected == result
    True
    >>> result = get_symbol_to_lines(('*', '*', '*', '*', '*'))
    >>> expected = {'*': [0, 1, 2, 3, 4]}
    >>> expected == result
    True
    """

    my_dict = {}
    new = unique_items(rhyme_scheme)
    for item in new:
        a = list_of_indices(item, rhyme_scheme)
        my_dict[item] = a
    return my_dict


def check_rhyme_scheme(poem_lines: POEM,
                       description: POETRY_FORM_DESCRIPTION,
                       word_to_phonemes: PRONUNCIATION_DICT) \
        -> List[List[POEM_LINE]]:
    """Return a list of lists of lines from poem_lines that do NOT rhyme with
    each other as specified by the poetry form description, according to the
    pronunciation dictionary word_to_phonemes. If all lines rhyme as they
    should, return the empty list.  The lines is each inner list should be
    in the same order as they appear in poem_lines.

    Precondition: len(poem_lines) == len(description[1])

    >>> poem_lines = ['The first line leads off,',
    ...               'With a gap before the next.', 'Then the poem ends.']
    >>> description = ((5, 7, 5), ('A', 'B', 'A'))
    >>> word_to_phonemes = {'NEXT': ('N', 'EH1', 'K', 'S', 'T'),
    ...                     'GAP': ('G', 'AE1', 'P'),
    ...                     'BEFORE': ('B', 'IH0', 'F', 'AO1', 'R'),
    ...                     'LEADS': ('L', 'IY1', 'D', 'Z'),
    ...                     'WITH': ('W', 'IH1', 'DH'),
    ...                     'LINE': ('L', 'AY1', 'N'),
    ...                     'THEN': ('DH', 'EH1', 'N'),
    ...                     'THE': ('DH', 'AH0'),
    ...                     'A': ('AH0'),
    ...                     'FIRST': ('F', 'ER1', 'S', 'T'),
    ...                     'ENDS': ('EH1', 'N', 'D', 'Z'),
    ...                     'POEM': ('P', 'OW1', 'AH0', 'M'),
    ...                     'OFF': ('AO1', 'F')}
    >>> bad_lines = check_rhyme_scheme(poem_lines, description,
    ...                                word_to_phonemes)
    >>> bad_lines.sort()
    >>> bad_lines
    [['The first line leads off,', 'Then the poem ends.']]
    """

    empty = []
    wrong_rhymes = []
    uniques = unique_items(description[1])
    for symbols in uniques:
        a = list_of_indices(symbols, description[1])
        empty.append(a)
    for i in empty:
        if all_lines_rhyme(poem_lines, i, word_to_phonemes) is False and \
           only_stars('*', description[1]) is False:
            b = subject_to_change(i, poem_lines)
            wrong_rhymes.append(b)
    return wrong_rhymes


if __name__ == '__main__':
    import doctest
    # Uncomment the line below if you prefer to test your examples with doctest
    # doctest.testmod()
