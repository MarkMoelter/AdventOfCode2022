import utils
from src.Day4 import PartialOverlap, TotalOverlap


def main():
    pairs = utils.read_input_file()

    # part 1
    print(TotalOverlap(pairs).overlap_score())

    # part 2
    print(PartialOverlap(pairs).overlap_score())


if __name__ == '__main__':
    main()
