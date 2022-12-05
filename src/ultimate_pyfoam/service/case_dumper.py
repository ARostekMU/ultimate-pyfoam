from dataclasses import dataclass
from pathlib import Path
from typing import Any
from typing import Mapping

from ultimate_pyfoam.domain.of_dict import OfDict
from ultimate_pyfoam.service.dumper import Dumper


@dataclass()
class CaseDumper:
    case: Mapping[str, Any]

    def dump(self, dump_dir: Path):
        for key, value in self.case.items():
            dumper = Dumper(value)
            dumper.write(dump_dir / key, True)
