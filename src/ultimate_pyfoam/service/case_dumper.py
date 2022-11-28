from dataclasses import dataclass
from pathlib import Path
from typing import Any
from typing import Mapping

from ultimate_pyfoam.domain.of_dict import OfDict
from ultimate_pyfoam.service.dumper import Dumper


@dataclass()
class CaseDumper:
    case: Mapping[Path, Mapping[str, Any]]

    def dump(self, dump_dir: Path) -> None:
        for path, content in self.case.items():
            dumper = Dumper(content=content)
            dumper.write(dump_dir / path)
