import logging
from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int = 0
    directory: bool = True
    contents: list = field(default_factory=list) if directory else None

    def add_file(self, file: str):
        """Add a file to the contents field."""
        size, name = file.split(' ')
        self.contents.append(file_factory(name, int(size)))

        logging.info(
            f'File "{name}", {size} bytes added to Directory "{self.name}"'
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
