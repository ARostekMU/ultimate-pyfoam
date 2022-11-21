from dataclasses import dataclass
from collections.abc import Mapping
from ultimate_pyfoam.domain.of_dict import OfDict
from pathlib import Path

@dataclass()
class Dumper:
    content: Mapping

    def write(self, path, overwrite=False) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and not path.is_dir() and not overwrite:
            raise FileExistsError('This file already exists. If you wish to overwrite, set "overwrite = True".')
        else:
            with path.open('w') as f:
                f.write(str(OfDict(self.content)))
