from dataclasses import dataclass
from pathlib import Path

from ultimate_pyfoam.domain.of_dict import OfDict


@dataclass()
class Dumper:
    content: OfDict

    def write(self, path: Path, overwrite: bool = False) -> None:

        if not path.exists() or overwrite:

            path.parent.mkdir(parents=True, exist_ok=True)

            with path.open("w") as f:

                f.write(str(OfDict(self.content)))

        elif path.exists() and not overwrite:

            if path.is_dir():

                raise (IsADirectoryError)

            else:

                raise (FileExistsError)
