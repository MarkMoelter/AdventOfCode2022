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

    def parse_initial_stack(self):
        pass
