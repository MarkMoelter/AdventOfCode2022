import utils
from Part1 import ParseInput
from Part2 import Part2


def main():
    # part 1
    print(ParseInput(utils.read_input_file()).parse_commands())

    # part 2
    print(Part2())


if __name__ == '__main__':
    main()
