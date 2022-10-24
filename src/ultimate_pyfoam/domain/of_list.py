from dataclasses import dataclass

# from typing import Any
from typing import List


@dataclass()
class OfList:
    name: str
    num_of_elements: int
    elements: List[int]

    def __str__(self) -> str:
        string = f"{self.name}"
        string += "\t("

        for i, element in enumerate(self.elements):
            if i != 0:
                string += " "
            string += str(element)

        string += "\n);"

        return string
