from dataclasses import dataclass


@dataclass
class Command:
    num_crates: int
    init_col: int
    dest_col: int
