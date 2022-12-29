import logging

import utils
from src.Day6 import first_unique_characters


def part_1():
    # get the first line of the input file.
    input_: str = utils.read_input_file()[0]

    print(first_unique_characters(input_))


def part_2():
    input_ = utils.read_input_file()[0]

    print(first_unique_characters(input_, 14))


def main():
    logging.basicConfig(level=logging.DEBUG)

    part_1()
    part_2()


if __name__ == '__main__':
    main()
