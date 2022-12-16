import utils


class TotalOverlap:
    def __init__(self, pairs: list[str] = None):
        self.pairs = pairs

    def process_input(self) -> list[tuple[set[int], ...]]:
        """
        Convert the raw list of lines into something meaningful.

        :return: A list containing assignment pairs converted into sets.
        """

        processed = []

        for pair in self.pairs:
            pair = pair.strip()

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

    def overlap_score(self) -> int:
        """
        Count the number of overlapping pairs in the input list.

        :return: The number of pairs that overlap completely.
        """

        score = 0

        # iterate over the pairs from the processed list
        for range_1, range_2 in self.process_input():

            # check if either range is a subset of the other
            if range_1.issubset(range_2) or range_2.issubset(range_1):
                score += 1

        return score
