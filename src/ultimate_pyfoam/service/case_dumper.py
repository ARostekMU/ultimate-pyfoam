from dataclasses import dataclass
from pathlib import Path
from typing import Any
from typing import Mapping

from ultimate_pyfoam.service.dumper import Dumper


@dataclass()
class CaseDumper:
    case: Mapping[Path, Mapping[str, Any]]

    def dump(self, dump_dir: Path) -> None:
        for rel_file_path, file_content in self.case.items():
            Dumper(content=file_content).write(dump_dir / rel_file_path)
