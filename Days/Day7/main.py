import logging

import utils
from Days.Day7 import create_file_system, size


def part_1():
    """Add up the file sizes with directories less than 10000 bytes."""
    input_ = utils.read_input_file()
    dirs, path = create_file_system(input_)
    candidates = []
    for d in dirs:
        files = size(d, dirs)
        if files <= 100000:
            candidates.append(files)
    print(sum(candidates))


def part_2():
    input_ = utils.read_input_file()
    dirs, path = create_file_system(input_)
    disk = 70000000
    needed = 30000000
    free = disk - size('/', dirs)

    candidates = []
    for d in dirs:
        files = size(d, dirs)
        if files + free >= needed:
            candidates.append(files)
    print(min(candidates))


def main():
    logging.basicConfig(level=logging.DEBUG)

    part_1()
    part_2()


if __name__ == '__main__':
    main()
