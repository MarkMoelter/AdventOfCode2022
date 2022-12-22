import re


def is_command(potential_command: str) -> bool:
    """Check if a string is considered a command"""
    regex_cmd = r'^\$\s[cdls]{2}(\s[a-zA-Z/\.]*)?$'
    return bool(re.search(regex_cmd, potential_command))


def is_file(potential_file: str) -> bool:
    """Check if a string is considered a file."""
    regex_file = r'^[0]*[1-9]+\d*\s[a-zA-Z]+(\.[a-zA-Z]{3})?$'
    return bool(re.search(regex_file, potential_file))


def is_directory(potential_directory: str) -> bool:
    """Check if a string is considered a directory."""
    regex_dir = r'^dir\s[a-zA-Z/]+$'
    return bool(re.search(regex_dir, potential_directory))


def file_structure(data_stream: list[str]) -> dict[str, list]:
    main_dir = '/'
    directories = {main_dir: []}

    # initialize the dictionary with all directories in the input
    for line in data_stream:
        if is_directory(line):
            dir_name: str = line.split()[1]

            directories[dir_name] = []

    current_directory = main_dir
    for line in data_stream:
        if is_command(line):
            cmd = line.split(line)

            if cmd[1] == 'cd':

                # changing current directory
                if cmd[2].isalpha() or cmd[2] == '/':
                    current_directory = cmd[2]

    return directories
