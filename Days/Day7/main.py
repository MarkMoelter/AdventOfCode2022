import utils
from Days.Day7 import ParseInput


def part_1():
    """Add up the file sizes with directories less than 10000 bytes."""
    input_ = utils.read_input_file('test_input.txt')
    print(ParseInput(input_).dirs)


def part_2():
    pass


def main():
    part_1()
    part_2()


if __name__ == '__main__':
    main()
