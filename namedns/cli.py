import click
from namedns.commands.record import record
from namedns.commands.domain import domain


@click.group()
def cli():
    pass

cli.add_command(record)
cli.add_command(domain)

if __name__ == '__main__':
    cli()
