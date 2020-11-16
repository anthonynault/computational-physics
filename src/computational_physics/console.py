import click

from . import __version__

import 

@click.command()
@click.version_option(version=__version__)
def main():
    """Computational physics."""
    click.echo("Hello, world!")