"""Console script for wizcoin."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for wizcoin."""
    click.echo("Replace this message by putting your code into "
               "wizcoin.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
