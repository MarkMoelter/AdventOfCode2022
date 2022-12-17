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

    def column_setup(self) -> dict[int: list[str]]:
        """
        The structure from the first 10 input lines.
        Represented as lists for each column.
        The beginning of each list is the bottom of each column.
        The input image can be visualized as rotating the
        dictionary 90 degrees counterclockwise.

        :return: A dictionary mapping the column integer
        to the blocks in that column.
        """

        col_dict = self._filter_input(col_num=9)

        # reverse list and remove all space characters
        for key, list_ in col_dict.items():
            list_.reverse()
            col_dict[key] = [ele for ele in list_ if ele != ' ']

        return col_dict

    def _filter_input(self, col_num: int, ) -> dict:
        """
        Lift most of the weight for column_setup method. Create the dictionary,
        loop though the lines of the input and

        :param col_num: The number of columns in the input diagram.
        :return: The dictionary
        """
        # initialize dictionary {1: [], 2: [], ...}
        col_dict = {i: [] for i in range(1, col_num + 1)}

        # loop through input rows
        for idx, row in enumerate(self.input_list):
            # ignore rows that are not important
            if idx + 1 >= 9:
                continue

            stripped_row = row.strip('\n')

            # 1, 5, 9, ..., len(row); n = (n-1) + 4
            important_indices = range(1, len(stripped_row), 4)

            # accumulate the relevant characters using a range
            for reg_idx, important_idx in enumerate(important_indices):
                # append the char at the important index to the list
                col_dict[reg_idx + 1].append(stripped_row[important_idx])

        return col_dict
