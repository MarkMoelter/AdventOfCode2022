from .block import Block
from .command import Command


class ParseInput:
    def __init__(self, input_list: list[str]):
        self.input_list = input_list

    @staticmethod
    def is_command(potential_command: list[str]) -> bool:
        """
        Check if a list of strings is considered a command.

        :param potential_command: The list to validate
        :return: Boolean indicating if it is considered a command
        """

        correct_length = len(potential_command) == 6
        move_exists = 'move' in potential_command
        from_exists = 'from' in potential_command
        to_exists = 'to' in potential_command

        return (
                correct_length
                and move_exists
                and from_exists
                and to_exists
        )

    def parse_commands(self) -> list[Command]:
        """
        Parses the valid commands from a list of human-readable command strings.

        :return: A list of command objects containing
        relevant information from each command.
        """
        commands = []

        for line in self.input_list:

            line = line.split(' ')

            # ignore non-command lines
            if not self.is_command(line):
                continue

            # remove extraneous strings from list
            line.remove('move')
            line.remove('from')
            line.remove('to')

            # map int() to each value
            int_values = map(int, line)

            # Upack values into Command, then append to list
            commands.append(Command(*int_values))

        return commands

    def column_setup(self) -> dict[int: list[Block]]:
        """
        The structure from the first 10 input lines.
        Represented as lists for each column.
        End of each list is the bottom of each column.

        :return: A dictionary mapping the column integer
        to the blocks in that column.
        """
        col_dict = {i: [] for i in range(1, 10)}
        col_list: list[list[str]] = []

        # loop through lines
        for i, row in enumerate(self.input_list):
            important_indices = list(range(1, len(row), 4))

            # remove lines that are not important
            if i + 1 >= 9:
                continue

            # convert str to single character list and remove newlines
            row = list(row.strip('\n'))

            # loop through characters in each line
            current = []
            for j, char in enumerate(row):

                # add characters that we care about
                if j in important_indices:
                    current.append(char)

            for j, char in enumerate(current):
                col_dict[j + 1].append(char)

        return col_dict
