from dataclasses import dataclass

from .block import Block


@dataclass
class Column:
    """Class for a column of the block structure"""
    column_number: int
    blocks: list[Block]
