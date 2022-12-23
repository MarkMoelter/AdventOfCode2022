from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int = 0
    contents: list = field(default_factory=list)

    def add_file(self):
        """Add a file to the contents field."""

    def change_working_directory(self, new_directory: str):
        """Change the working directory."""


@dataclass
class Directory:
    name: str
    files: list[File] = field(default_factory=list)
    sub_directories: list = field(default_factory=list)

    def file_size(self) -> int:
        """
        Return the size of the files in the directory.
        Does not include subdirectories.

        :return: The total in bytes of all files in the directory.
        """
        return sum([file.size for file in self.files])
