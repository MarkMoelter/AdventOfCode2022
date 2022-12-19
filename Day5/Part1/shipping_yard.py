from .command import Command


class ShippingYard:
    def __init__(self, columns: dict = None):
        self.columns = columns

    def get_yard(self) -> dict:
        """Print the columns using pretty print."""
        return self.columns

    def move_crates(self, cmd: Command) -> None:
        """Move blocks between columns. Alter the state of the columns."""
        # the column to change
        init_column = self.columns[cmd.initial_column]

        # the crates to move from that column
        crates = init_column[-cmd.blocks_to_move:]

        # remove the values from the column
        self.columns[cmd.initial_column] = init_column[:-cmd.blocks_to_move]

        # add the crates to the destination column
        for crate in crates:
            self.columns[cmd.destination_column].append(crate)
