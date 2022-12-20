import logging

import utils
from Day5 import ParseInput, Part2, ShippingYard


def part_1():
    logging.info('Starting part 1')
    input_ = utils.read_input_file()

    parse = ParseInput(input_)
    yard = ShippingYard(parse.column_setup())

    # move crates according to commands
    for i, cmd in enumerate(parse.parse_commands()):
        logging.debug(cmd)
        yard.move_crates(cmd)

    # final image
    print(''.join(yard.last_in_each_column()))

    logging.info('Finishing part 1')


def part_2():
    print(Part2())


def main():
    logging.basicConfig(level=logging.INFO)

    part_1()
    part_2()


if __name__ == '__main__':
    main()
