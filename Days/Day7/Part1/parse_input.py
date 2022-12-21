from .data_structures import Directory, File

class ParseInput:
    def __init__(self, data_stream: list[str]) -> None:
        self.data_stream = data_stream

    def directories(self) -> dict[Directory, list[Directory]]:
        """Parse the data stream into a dictionary
        that maps directories to subdirectories."""
        pass


    def files(self) -> dict[File, Directory]:
        """Parse the data stream into a dictionary
        that maps a file to its directory."""
        pass