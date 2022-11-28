"""Command-line interface."""
import sys
from importlib import import_module
from pathlib import Path

import click

from ultimate_pyfoam.service.case_dumper import CaseDumper


@click.version_option()
@click.group()
def main() -> None:
    """Ultimate PyFoam!!!."""


@main.command()
@click.argument("input_file", type=Path, default="case.py")
@click.argument("output_dir", type=Path, default="of_case")
def dump(input_file: Path, output_dir: Path) -> None:
    sys.path.append(str(input_file.parent))

    case = import_module(input_file.stem)
    case_dumper = CaseDumper(case.case)
    case_dumper.dump(output_dir)


if __name__ == "__main__":
    main(prog_name="ultimate-pyfoam")  # pragma: no cover
