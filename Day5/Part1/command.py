from dataclasses import dataclass


@dataclass
class Command:
    blocks_to_move: int
    initial_column: int
    destination_column: int
