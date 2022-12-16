import utils
from Day5 import ParseInput, Part2


def main():
    # part 1
    print(ParseInput(utils.read_input_file()).parse_commands())

    # part 2
    print(Part2())


if __name__ == '__main__':
    main()
