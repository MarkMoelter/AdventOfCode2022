from pprint import pprint

import utils
from Day5 import ParseInput, Part2, ShippingYard


def main():
    input_ = utils.read_input_file()

    parse = ParseInput(input_)
    yard = ShippingYard(parse.column_setup())

    # starting image
    pprint(parse.column_setup())

    # part 1
    # move crates according to commands
    for cmd in parse.parse_commands():
        yard.move_crates(cmd)

    # final image
    pprint(yard.get_yard())

    # part 2
    print(Part2())


if __name__ == '__main__':
    main()
