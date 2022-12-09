def read_input_file() -> list[str]:
    """Read the lines of the input file and remove newlines.

    :return: A list containing the lines of the file as the elements.
    """
    with open('input.txt', 'r') as f:
        return [ele.strip() for ele in f.readlines()]


def individual_elves() -> dict[int: int]:
    """
    Separate the list of input elements into individual elves at the blank lines.

    :return: A dictionary that represents individual elves.
    """
    elf_id = 1
    elf_dict = {}
    current_elf = []

    for item in read_input_file():

        # append item to list if item is not a blank string
        if item != '':
            current_elf.append(int(item))

        # copy current elf list into dict, increase the key count and clear the current list
        else:
            elf_dict[elf_id] = sum(current_elf)
            elf_id += 1
            current_elf.clear()

    return elf_dict


def elf_with_most_calories() -> tuple[int, int]:
    """
    Finds the elf with the most calories on his/her person.

    :return: The elf's id and his/her total number of calories.
    """
    elf_id = None
    most_calories = None

    for key, calorie_count in individual_elves().items():

        # initialize the id and calorie amount
        if elf_id is None:
            elf_id = key
            most_calories = calorie_count

        if most_calories < calorie_count:
            elf_id = key
            most_calories = calorie_count

    return elf_id, most_calories


def top_elves(top_number: int) -> list[int]:
    """
    Calculate the top three elves holding the most calories.

    :return: A list containing 3 values that represent the 3 elves with the largest amount.
    """
    sorted_dict = sorted(individual_elves().values(), reverse=True)

    return [sorted_dict[i] for i in range(top_number)]


def main():
    # part 1
    print(elf_with_most_calories()[1])
    # or
    print(*top_elves(1))

    # part 2
    print(sum(top_elves(3)))


if __name__ == '__main__':
    main()
