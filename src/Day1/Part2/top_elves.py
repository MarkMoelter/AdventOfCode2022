from src.Day1.Part1 import separate_elves


def top_elves(top_number: int) -> list[int]:
    """
    Calculate the top three elves holding the most calories.

    :return: A list containing 3 values that represent the 3 elves with the largest amount.
    """
    sorted_dict = sorted(separate_elves().values(), reverse=True)

    return [sorted_dict[i] for i in range(top_number)]
