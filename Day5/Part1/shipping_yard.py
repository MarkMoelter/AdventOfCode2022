# TODO:
#  Step 1) Process input to separate column structure and commands - done
#  Step 2) Store blocks, columns, and commands as objects
#  Step 3) Move blocks between columns according to commands


from .command import Command
from pprint import pprint

class ShippingYard:
    def __init__(self, columns: dict):
        self.columns = columns

    def get_yard(self) -> dict:
        """Print the columns using pretty print."""
        return self.columns

    def move_crates(self, command: Command) -> None:
        """Move blocks between columns. Alter the state of the columns."""
        pass
