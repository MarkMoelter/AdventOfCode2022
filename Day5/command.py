from dataclasses import dataclass


@dataclass
class Command:
    blocks_to_move: int
    starting_column: int
    destination_column: int
