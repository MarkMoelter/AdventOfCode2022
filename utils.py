def read_input_file() -> list[str]:
    """
    Read the lines of the input file and remove newlines.

    :return: A list containing the lines of the file as the elements.
    """
    with open('input.txt', 'r') as f:
        return [ele.strip() for ele in f.readlines()]
