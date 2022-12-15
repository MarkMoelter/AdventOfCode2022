from dataclasses import dataclass


@dataclass
class Block:
    column: int
    row: int
    value: str
