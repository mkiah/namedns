import click
from commands.record import record
from commands.domain import domain


@click.group()
def cli():
    pass

cli.add_command(record)
cli.add_command(domain)

if __name__ == '__main__':
    cli()
