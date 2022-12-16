import utils


def separate_elves() -> dict[int: int]:
    """
    Separate the list of input elements into individual elves at the blank lines.

    :return: A dictionary that represents individual elves.
    """
    elf_id = 1
    elf_dict = {}
    current_elf = []

    for item in utils.read_input_file():

        # append item to list if item is not a blank string
        if item != '':
            current_elf.append(int(item))

        # copy current elf list into dict, increase the key count and clear the current list
        else:
            elf_dict[elf_id] = sum(current_elf)
            elf_id += 1
            current_elf.clear()

    return elf_dict
