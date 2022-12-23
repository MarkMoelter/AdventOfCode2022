import re

from .data_structures import File


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


def create_file_system(data_stream: list[str]) -> File:
    """Create the file system from the commands given."""
    root = File('/')
    working_directory = root
    for line in data_stream:
        # change working directory
        if line.startswith('$ cd '):
            working_directory = root.change_working_directory(line[5:])
        elif line.startswith('$ ls'):
            continue
        else:
            working_directory.add_file(line)
    return root
