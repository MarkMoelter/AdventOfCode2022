def size(folder, structure) -> int:
    """Calculate the size of folder and files in structure."""
    total = 0
    for ele in structure[folder]:
        if ele[0] == 'dir':
            total += size(ele[1], structure)
        else:
            total += int(ele[0])

    return total
