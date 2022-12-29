import re

from .file import File


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
        elif is_file(line):
            working_directory.add_file(line)
    return root
