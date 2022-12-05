"""Command-line interface."""
import click
import importlib
from pathlib import Path
from ultimate_pyfoam.service.case_dumper import CaseDumper


@click.group()
@click.version_option()
def main() -> None:
    """Ultimate PyFoam!!!."""


@main.command
@click.argument('case_file', default="case.py")
def dump():
    click.echo("aaa")

    module = importlib.util.spec_from_file_location('case_file')
    case = module.__getattr__("case")

    cd = CaseDumper(case)
    #cd.dump(temp_dir)

    return 0


if __name__ == "__main__":
    main(prog_name="ultimate-pyfoam")  # pragma: no cover
