def read_input_file() -> list[str]:
    """Read the lines of the input file and remove newlines.

    :return: A list containing the lines of the file as the elements.
    """
    with open('input.txt', 'r') as f:
        return [ele.strip() for ele in f.readlines()]


def individual_elves() -> dict[int: list[int]]:
    """Return a dict of lists that represent individual elves."""
    # iterate through the input list to separate elves at blank elements.
    elf_id = 0
    elf_dict = {}

    current_elf = []
    for item in read_input_file():

        if item != '':
            current_elf.append(int(item))

        else:
            elf_dict[elf_id] = current_elf.copy()
            elf_id += 1
            current_elf.clear()

    return elf_dict


def main():
    print(len(individual_elves()))


if __name__ == '__main__':
    main()
