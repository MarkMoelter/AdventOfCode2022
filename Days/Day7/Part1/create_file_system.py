from .file import File


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
