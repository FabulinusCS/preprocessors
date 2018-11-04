# -*- coding: utf-8 -*-

"""Console script for preprocessors."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for preprocessors."""
    click.echo("Replace this message by putting your code into "
               "preprocessors.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
