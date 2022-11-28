from pathlib import Path

import click

from ultimate_pyfoam.service.case_dumper import CaseDumper


@click.group()
def main() -> None:
    """Ultimate PyFoam!"""
    pass


@click.command()
@click.argument(
    "case-file",
    default="case.py",
    type=click.Path(exists=True),
)
@click.argument(
    "dump-dir",
    default="of_case",
)
def dump(case_file: Path, dump_dir: str) -> None:
    click.echo("This subcommand should dump something...")

    import sys

    sys.path.insert(0, str(Path(case_file).parent))
    import importlib

    module = importlib.import_module(Path(case_file).stem)
    case_var_name = "case"
    case = getattr(module, case_var_name)

    CaseDumper(case=case).dump(dump_dir=Path(dump_dir))


main.add_command(dump)


if __name__ == "__main__":
    main()
