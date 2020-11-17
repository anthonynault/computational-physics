import click

from . import __version__

from computational_physics

@click.command()
@click.version_option(version=__version__)
def main():
    """Computational physics."""
    click.echo("Hello, world!")