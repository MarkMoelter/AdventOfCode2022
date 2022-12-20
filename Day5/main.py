import logging
from pprint import pprint

import utils
from Day5 import ParseInput, Part2, ShippingYard


def main():
    logging.basicConfig(level=logging.DEBUG)

    input_ = utils.read_input_file()

    parse = ParseInput(input_)
    yard = ShippingYard(parse.column_setup())

    # part 1
    # move crates according to commands
    for i, cmd in enumerate(parse.parse_commands()):
        logging.debug(i)
        yard.move_crates(cmd)

    # final image
    print(''.join(yard.last_in_each_column()))

    # part 2
    print(Part2())


if __name__ == '__main__':
    main()
