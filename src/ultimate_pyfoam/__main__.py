"""Command-line interface."""
import click
import ultimate_pyfoam.domain


@click.command()
@click.version_option()
@click.argument("arg")
@click.option("--name", default="Default", help="Help message", show_default=True)
@click.option("--prompt", prompt=True)
def main(arg, name, prompt) -> None:
    """Ultimate PyFoam!!!."""
    print(arg)
    print(name)
    print(prompt)


if __name__ == "__main__":
    main(prog_name="ultimate-pyfoam")  # pragma: no cover
