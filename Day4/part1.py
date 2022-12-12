# TODO: Collect the input pairs
# TODO: Convert ranges into sets
# TODO: Check if range pairs are subsets
# TODO: Count how many pairs one range fully contains the other

import utils


class CampCleanup:
    def __init__(self, pairs: list[str] = None):
        self.pairs = pairs

    def process_input(self) -> list[tuple[set[int], set[int]]]:
        """
        Convert the raw list of lines into something meaningful.

        :return: A list containing assignment pairs converted into sets.
        """

        return []


def main():
    pairs = utils.read_input_file()
    part_1 = CampCleanup(pairs)


if __name__ == '__main__':
    main()
