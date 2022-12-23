import logging
import re
from dataclasses import dataclass, field


def is_file(potential_file: str) -> bool:
    """Check if a string is considered a file."""
    regex_file = r'^[0]*[1-9]+\d*\s[a-zA-Z]+(\.[a-zA-Z]{3})?$'
    return bool(re.search(regex_file, potential_file))


@dataclass
class File:
    name: str
    size: int = 0
    contents: list = field(default_factory=list)
    directory: bool = True

    def add_file(self, file_to_add: str):
        """Add a file to the contents field."""
        if is_file(file_to_add):
            size, name = file_to_add.split()
            self.contents.append(file_factory(name, size))

            logging.info(
                f'File "{name}", {size} bytes added to Directory "{File.name}"'
            )

    def change_working_directory(self, new_directory: str):
        """Change the working directory and return a file object."""

    def find_folders(self, max_size: int) -> list:
        """Find all the folders in the file system with size <= max_size."""

    def calc_size(self) -> int:
        """Calculate the size of the folders and files in the current folder."""
        return sum([file.size for file in self.contents])


def file_factory(filename: str, file_size: int) -> File:
    """Return a file object"""
    return File(filename, file_size, directory=False)
