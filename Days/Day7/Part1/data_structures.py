from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int


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
