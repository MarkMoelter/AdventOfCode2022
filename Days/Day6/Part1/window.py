def sliding_window(input_string: str, window_size: int = 4) -> int:
    """
    Check where the input string has unique characters.

    :param input_string: The string to check for unique characters.
    :param window_size: The number of characters that need to be unique before
    returning.
    :return: The index of the input string where the input string has unique
    characters equal to the window size.
    """

    # catch case input shorter than window size
    if len(input_string) < window_size:
        raise ValueError(
            f'Provided string must be longer than window size {window_size}.'
        )

    for i in range(len(input_string) - window_size + 1):
        left = i
        right = window_size + i

        if is_unique(*input_string[left:right]):
            return right

    raise ValueError(
        'The input string does not contain unique characters'
        ' with the chosen window size.'
    )


def is_unique(*characters: str) -> bool:
    """
    Check if the provided characters are unique from each other.
    Compare the length of a set with the length of a list with the characters.
    If both are the same length, all characters are unique.

    :param characters: The characters to check for uniqueness.
    :return: True if the characters are unique
    """

    return len({*characters}) == len([*characters])
