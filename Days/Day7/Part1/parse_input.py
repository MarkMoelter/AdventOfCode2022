import re

from .data_structures import File, Directory


def is_command(potential_command: str) -> bool:
    """
    Check if a string is considered a command.

    Checks for a '$' to start the string, a space, then a cd or ls
     command, then an optional directory after the command.
    Format: '$ cd/ls opt(directory)'

    :param potential_command: The string to check.
    :return: True if the string is a command, False otherwise.
    """
    regex_cmd = r'^\$\s(cd|ls)(\s[a-zA-Z/\.]*)?$'
    return bool(re.search(regex_cmd, potential_command))


def is_file(potential_file: str) -> bool:
    """Check if a string is considered a file."""
    regex_file = r'^[0]*[1-9]+\d*\s[a-zA-Z]+(\.[a-zA-Z]{3})?$'
    return bool(re.search(regex_file, potential_file))


def is_directory(potential_directory: str) -> bool:
    """Check if a string is considered a directory."""
    regex_dir = r'^dir\s[a-zA-Z/]+$'
    return bool(re.search(regex_dir, potential_directory))


def get_dir_name(directory_command: str) -> str:
    """Get the directory name from the given command."""

    # TODO: handle 'x' and '..'
    pot_dir = directory_command.split(' ')[-1]

    result = re.search(r'[a-zA-Z/]+$', pot_dir)
    if result:
        return result[0]

    raise ValueError(f'The directory command, {directory_command} does not have a valid directory name')


class ParseInput:
    def __init__(self, data_stream: list[str]):
        self.data_stream = data_stream
        self.dirs = self._parse_directories()

    def _parse_directories(self) -> list[Directory]:
        """
        Create a dictionary mapping the directories to empty lists.

        Does not map directories to other directories or files yet.

        :return: A dictionary containing all the directories and empty lists
        """
        directories = [Directory('/')]

        for line in self.data_stream:
            if not is_directory(line):
                continue

            dir_name = get_dir_name(line)
            directories.append(Directory(dir_name))

        return directories

    def parse_files(self) -> None:
        """Add files to the appropriate directories."""
        current_dir = '/'

        for line in self.data_stream:
            # change directory
            if is_command(line):
                command = line.split(' ')
                cd_cmd = command[1] == 'cd'
                x = command[2] == 'x'
                dotdot = command[2] == '..'

                if cd_cmd and not x and not dotdot:
                    current_dir = get_dir_name(line)

            # add files to directory
            elif is_file(line):
                size, filename = line.split(' ')
                self.dirs[current_dir].files.append(File(filename, size))
