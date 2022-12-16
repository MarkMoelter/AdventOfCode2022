from .block import Block
from .command import Command
from .mover import Mover
from .parse_input import ParseInput


def column_setup() -> dict[int: list[Block]]:
    """
    The structure from the first 10 input lines.
    Represented as lists for each column.

    :return: A dictionary mapping the column integer to the blocks in that column.
    """
