import utils
from Day5 import ParseInput, Part2
from pprint import pprint


def main():
    input_ = utils.read_input_file()

    # part 1
    pprint(ParseInput(input_).column_setup())
    # print(ParseInput(input_).parse_commands())

    # part 2
    print(Part2())


if __name__ == '__main__':
    main()
