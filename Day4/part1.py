# TODO: Collect the input pairs
# TODO: Convert ranges into sets
# TODO: Check if range pairs are subsets
# TODO: Count how many pairs one range fully contains the other

import utils


class CampCleanup:
    def __init__(self, pairs: list[str] = None):
        self.pairs = pairs

    def process_input(self) -> list[tuple[set[int], ...]]:
        """
        Convert the raw list of lines into something meaningful.

        :return: A list containing assignment pairs converted into sets.
        """

        processed = []

        for pair in self.pairs:
            # split into ranges
            current = []
            for range_ in pair.split(','):
                # split ranges into upper and lower bounds
                lower, upper = range_.split('-')
                # convert bounds to the actual range values
                set_val = {*range(int(lower), int(upper) + 1)}
                current.append(set_val)

            processed.append(tuple(current.copy()))
            current.clear()

        return processed

    def total_overlapping_pairs(self) -> int:
        """
        Count the number of overlapping pairs in the input list.

        :return: The number of pairs that overlap completely.
        """

        return 0


def main():
    pairs = utils.read_input_file()
    part_1 = CampCleanup(pairs)
    print(part_1.process_input())


if __name__ == '__main__':
    main()
