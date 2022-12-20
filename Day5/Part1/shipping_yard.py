import logging

from .command import Command


class ShippingYard:
    def __init__(self, columns: dict[int, list[str]]):
        self.columns = columns

    def get_yard(self) -> dict[int, list[str]]:
        """Return the columns object as a dictionary."""
        return self.columns

    def move_crates(self, cmd: Command) -> None:
        """Move blocks between columns. Alter the state of the columns."""
        # the column to change
        init_column = self.columns[cmd.init_col]

        # use list slicing to separate the crates into two lists
        crates_to_move = init_column[-cmd.num_crates:]
        crates_to_move.reverse()
        updated_column = init_column[:-cmd.num_crates]

        # add the crates to the destination column
        self.columns[cmd.dest_col] += crates_to_move

        # remove the crates from the column
        self.columns[cmd.init_col] = updated_column

        logging.debug('Initial column')
        logging.debug(init_column)
        logging.debug('List of crates to move')
        logging.debug(crates_to_move)
        logging.debug('Updated column')
        logging.debug(self.columns[cmd.init_col])

    def last_in_each_column(self) -> list[str]:
        """
        Get the last value in each column.

        :return: A list with the last value of each column.
        """
        return [col[-1] for col in self.columns.values()]
