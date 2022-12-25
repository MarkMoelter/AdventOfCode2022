import logging

import utils
from Days.Day8 import Visibility


def part_1():
    """Determine how many trees are visible from outside the grid."""
    forest = utils.read_input_file('test_input.txt')
    vis = Visibility(forest)
    print(vis.count_visible_trees())


def part_2():
    pass


def main():
    logging.basicConfig(level=logging.DEBUG)
    part_1()
    part_2()


if __name__ == '__main__':
    main()
