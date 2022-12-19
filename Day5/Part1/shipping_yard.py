# TODO:
#  Classes needed:
#  Blocks() for keeping track of each block's state
#  Stack() to keep track of each stack of blocks
#  Command() to track:
#       how many blocks to move,
#       starting column,
#       destination column

# TODO:
#  Step 1) Process input to separate column structure and commands - done
#  Step 2) Store blocks, columns, and commands as objects
#  Step 3) Move blocks between columns according to commands


from .command import Command
from pprint import pprint

class ShippingYard:
    def __init__(self, columns: dict):
        self.columns = columns

    def move_crates(self, command: Command) -> None:
        """Move blocks between columns. Alter the state of the columns."""
        pass

    def print_columns(self) -> None:
        """Print the columns using pretty print."""
        pprint(self.columns)
