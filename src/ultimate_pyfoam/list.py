from dataclasses import dataclass
from typing import Sequence

@dataclass()
class OfList():
    name:str
    content:Sequence

    def __str__(self):
        string = f'self.name'
        string += ' (\n'
        for entry in content:
            string += f'entry\n'
        string += ');' 