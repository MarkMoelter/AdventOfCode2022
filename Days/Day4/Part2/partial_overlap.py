import utils
from Days.Day4 import TotalOverlap


class PartialOverlap(TotalOverlap):
    def overlap_score(self) -> int:
        score = 0

        for set_1, set_2 in self.process_input():
            # use union to check if sets overlap
            if not set_1.isdisjoint(set_2):
                score += 1

        return score


def main():
    pairs = utils.read_input_file()
    partial = PartialOverlap(pairs)
    overlap_count = partial.overlap_score()

    print(overlap_count)


if __name__ == '__main__':
    main()
