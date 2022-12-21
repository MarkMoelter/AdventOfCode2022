import logging


def window_func(input_string: str, window_size: int = 4) -> int:
    """
    Check where the input string has unique characters.

    :param input_string: The string to check for unique characters.
    :param window_size: The number of characters that need to be unique before
    returning.
    :return: The index of the input string where the input string has unique
    characters equal to the window size.
    """

def is_unique(*characters: str) -> bool:
    """
    Check if the provided characters are unique from each other.
    Compare the length of a set with the length of a list with the characters.
    If both are the same length, all characters are unique.

    :param characters: The characters to check for uniqueness.
    :return: True if the characters are unique
    """

    return len({*characters}) == len([*characters])
