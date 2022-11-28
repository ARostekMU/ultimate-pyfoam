from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

from ultimate_pyfoam.domain.of_dict import OfDict


@dataclass()
class Dumper:
    content: Mapping

    def write(self, path: Path, overwrite: bool = False) -> None:
        if path.is_dir():
            raise IsADirectoryError

        if path.is_file() and overwrite is False:
            raise FileExistsError

        if not path.parent.exists():
            path.parent.mkdir(parents=True)

        with path.open("w") as f:
            f.write(str(OfDict(self.content)))
