import utils
from command import Command


def parse_commands(input_list: list[str]) -> list[Command]:
    commands = []

    for line in input_list:

        split_line = line.split(' ')

        # ignore non-command lines
        if split_line[0] != 'move':
            continue

        # remove extraneous strings from list
        split_line.remove('move')
        split_line.remove('from')
        split_line.remove('to')

        # map int() to each value
        int_values = map(int, split_line)

        # Upack values into Command, then append to list
        commands.append(Command(*int_values))

    return commands


def main():
    print(parse_commands(utils.read_input_file()))


if __name__ == '__main__':
    main()
