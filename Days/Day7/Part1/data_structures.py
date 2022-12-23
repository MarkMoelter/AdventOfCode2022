from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int = 0
    contents: list = field(default_factory=list)
    directory: bool = True

    def add_file(self, file_to_add) -> None:
        """Add a file to the contents field."""

    def change_working_directory(self, new_directory: str):
        """Change the working directory and return a file object."""

    def find_folders(self, max_size: int) -> list:
        """Find all the folders in the file system with size <= max_size."""

    def calc_size(self) -> int:
        """Calculate the size of the folders and files in the current folder."""
        return sum([file.size for file in self.contents])
