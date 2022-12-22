def is_command(str_: str) -> bool:
    """Check if a string is considered a command"""
    return str_.startswith('$')


def is_file(str_: str) -> bool:
    """Check if a string is considered a file."""
    return str_[0].isdigit()


def is_directory(str_: str) -> bool:
    """Check if a string is considered a directory."""
    return str_.startswith('dir')


def file_structure(data_stream: list[str]) -> dict[str, list]:
    main_dir = '/'
    directories = {main_dir: []}

    # initialize the dictionary with the directories
    for line in data_stream:
        if is_directory(line):
            dir_name: str = line.split()[1]

            directories[dir_name] = []

    # current_directory = main_dir
    #
    # for line in data_stream:
    #     if is_directory(line):
    #         pass
    #
    #     elif is_file(line):
    #         size, name = line.split(' ')
    #
    #         directories['/'].append(File(name, size))
    #     elif is_command(line):
    #         pass

    return directories
