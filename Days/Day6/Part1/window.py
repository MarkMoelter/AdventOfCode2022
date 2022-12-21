def first_unique_characters(input_string: str, window_size: int = 4) -> int:
    """
    Check where the input string has unique characters.
    The return value starts at 1 not 0.

    :param input_string: The string to check for unique characters.
    :param window_size: The number of characters that need to be unique before
    returning.
    :return: The index of the input string where the first set of unique
    characters equal to the window size were found.
    """

    # catch case input shorter than window size
    if len(input_string) < window_size:
        raise ValueError(
            f'Provided string must be longer than window size, {window_size}.'
        )

    # use the sliding window algorithm
    for i in range(len(input_string) - window_size + 1):

        # initialize the pointers
        left = i
        right = window_size + i

        window: str = input_string[left:right]

        # return the right pointer when a unique window is found
        if is_unique(*window):
            return right

    # raise error if no unique set of the window size is found
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
