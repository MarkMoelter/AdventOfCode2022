from .separate_elves import separate_elves


def elf_with_most_calories() -> tuple[int, int]:
    """
    Finds the elf with the most calories on his/her person.

    :return: The elf's id and his/her total number of calories.
    """
    elf_id = None
    most_calories = None

    for key, calorie_count in separate_elves().items():

        # initialize the id and calorie amount
        if elf_id is None:
            elf_id = key
            most_calories = calorie_count

        if most_calories < calorie_count:
            elf_id = key
            most_calories = calorie_count

    return elf_id, most_calories