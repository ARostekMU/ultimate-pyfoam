from dataclasses import InitVar
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Any
from typing import Mapping

from ultimate_pyfoam.domain.of_dict import OfDict


@dataclass()
class Dumper:
    content: InitVar[Mapping[str, Any]]
    content_ofdict: OfDict = field(init=False)

    def __post_init__(self, content: Mapping[str, Any]) -> None:
        self.content_ofdict = OfDict(content)

    def write(self, path: Path, overwrite: bool = False) -> None:
        if path.is_dir():
            raise IsADirectoryError()

        if not overwrite and path.exists():
            raise FileExistsError()

        if not path.parent.exists():
            path.parent.mkdir(parents=True)

        with path.open("w") as f:
            f.write(str(self.content_ofdict))
