from dataclasses import dataclass
from pathlib import Path

from ultimate_pyfoam.domain.of_dict import OfDict


@dataclass()
class Dumper:
    path: Path
    content: OfDict
    overwrite: bool = False

    def write(self) -> None:
        if self.path.is_dir():
            raise IsADirectoryError

        if not self.overwrite and self.path.exists():
            raise FileExistsError

        self.path.parents[0].mkdir(parents=True, exist_ok=True)

        with self.path.open("w") as output:
            output.write(str(self.content))
