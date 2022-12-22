from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str

