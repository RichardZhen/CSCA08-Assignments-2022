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

from typing import TextIO

from poetry_constants import (POETRY_FORMS_DICT, PRONUNCIATION_DICT)


# ===================== Add Your Helper Functions Here =====================

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


def entries_list_to_tuple(change: dict[str, list]) -> dict[str, tuple]:
    """ Change the values of keys that are list to tuple
    ... change = {'ABSINTHE': ['AE1', 'B', 'S', 'IH0', 'N', 'TH'], 'HEART':
    ...   ['HH', 'AA1', 'R', 'T'], 'FONDER': ['F', 'AA1', 'N', 'D', 'ER0']}
    >>> entries_list_to_tuple(change)
    ...   {'ABSINTHE': ('AE1', 'B', 'S', 'IH0', 'N', 'TH'), 'HEART':
    ...   ('HH', 'AA1', 'R', 'T'), 'FONDER': ('F', 'AA1', 'N', 'D', 'ER0')}
    """

    tpl = ()

    for key in change:
        for item in change[key]:
            a = string_into_tuple(item)
            tpl += a
            change[key] = tpl
        tpl = ()
    return change


def cnvrt_pf_description(poetry_forms_file: TextIO) -> \
                            tuple[tuple[int], tuple[str]]:
    """
    Return POETRY_FORM_DESCRIPTION from poetry_forms_file

    """

    syllable_count = ()
    rhyme_pattern = ()
    T = True

    while T is True:
        line = poetry_forms_file.readline().rstrip('\n')
        if len(line) == 0:
            T = False
        else:
            line_lst = line.split()
            syllable_count += (int(line_lst[0]),)
            rhyme_pattern += (line_lst[1],)
    return syllable_count, rhyme_pattern

# ===================== Required Functions =================================


def read_pronunciation(pronunciation_file: TextIO) -> PRONUNCIATION_DICT:
    """Return the pronunciation dictionary formed from reading
    pronunciation_file, an open file that is in the format of the CMU
    Pronouncing Dictionary.

    >>> small_pd = open('datasets/pronunciation_dictionary_small.txt')
    >>> word_to_phonemes = read_pronunciation(small_pd)
    >>> small_pd.close()
    >>> word_to_phonemes == {'CAMPBELL': ('K', 'AE1', 'M', 'B', 'AH0', 'L'),
    ...                      'GRIES': ('G', 'R', 'AY1', 'Z'),
    ...                      'SMITH': ('S', 'M', 'IH1', 'TH')}
    True
    """

    dic = {}
    for lines in pronunciation_file:
        if lines[0:3] != ';;;':
            replace = lines.split()
            word = replace[0]
            syllables = replace[1:]
            dic[word] = syllables
    dict_phonemes = entries_list_to_tuple(dic)
    return dict_phonemes


def read_poetry_form_descriptions(poetry_forms_file: TextIO) \
        -> POETRY_FORMS_DICT:
    """Return a dictionary of poetry form name to poetry form description for
    the poetry forms in poetry_forms_file.

    >>> small_pf = open('datasets/poetry_forms_small.txt')
    >>> name_to_description = read_poetry_form_descriptions(small_pf)
    >>> small_pf.close()
    >>> name_to_description == {
    ...     'Haiku': ((5, 7, 5), ('*', '*', '*')),
    ...     'Limerick': ((8, 8, 5, 5, 8), ('A', 'A', 'B', 'B', 'A'))}
    True
    """

    poetry_keys = []
    pfd = []
    poetry_forms_dict = {}
    count = 0
    for line in poetry_forms_file:
        poetry_keys += (line.rstrip('\n'), )
        pfd += (cnvrt_pf_description(poetry_forms_file), )
    for key in poetry_keys:
        description = pfd[count]
        poetry_forms_dict[key] = description
        count += 1
    return poetry_forms_dict


if __name__ == '__main__':
    import doctest
    # Uncomment the line below if you prefer to test your examples with doctest
    # doctest.testmod()
