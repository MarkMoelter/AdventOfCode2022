def create_file_system(data_stream: list[str]) -> tuple[dict, list]:
    """Create the file system from the commands given."""
    dirs = {}
    path = []
    for line in data_stream:
        cmd_mode = line.startswith('$')
        if cmd_mode:
            if line.startswith('$ cd '):
                directory = line.split(' ')[2]
                if directory == '..':
                    path.pop()
                else:
                    path.append(directory)
        else:
            cwd = '-'.join(path)
            files = dirs.get(cwd, [])
            atom = line.split()
            if atom[0] == 'dir':
                atom[1] = f'{cwd}-{atom[1]}'
            files.append(atom)
            dirs[cwd] = files

    return dirs, path
