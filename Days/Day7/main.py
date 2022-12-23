import logging

import utils
from Days.Day7 import create_file_system


def part_1():
    """Add up the file sizes with directories less than 10000 bytes."""
    input_ = utils.read_input_file('test_input.txt')
    root = create_file_system(input_)
    delete_me = root.find_folders(100_000)
    print(f'The size to delete: {sum([file.calc_size() for file in delete_me])}')


def part_2():
    pass


def main():
    logging.basicConfig(level=logging.DEBUG)

    part_1()
    part_2()


if __name__ == '__main__':
    main()
