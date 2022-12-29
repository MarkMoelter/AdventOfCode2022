import utils
from src.Day3 import RucksackCheck, RucksackGroups


def main():
    rucksacks = utils.read_input_file()
    # part 1
    print(RucksackCheck(rucksacks).total_priority())

    # part 2
    print(RucksackGroups(rucksacks).total_priority())


if __name__ == '__main__':
    main()
