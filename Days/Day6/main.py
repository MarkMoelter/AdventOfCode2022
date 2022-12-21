import logging

import utils
from Days.Day6 import sliding_window


def part_1():
    # TODO: create a window function that searches for the first 4 unique characters in the input.
    #  Will probably use sets and check for the length of the window set == 4.
    #  Meaning there are 4 unique characters. Keep track of the index where it occurs.
    # get the first line of the input file.
    input_: str = utils.read_input_file()[0]

    print(sliding_window(input_))

def part_2():
    input_ = utils.read_input_file()


def main():
    logging.basicConfig(level=logging.DEBUG)

    part_1()
    part_2()


if __name__ == '__main__':
    main()
