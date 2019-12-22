import click
from namedns.commands.record import record
from namedns.commands.domain import domain
from namedns import namedns

# Need to add ability to get credentials from ENV or config
# https://click.palletsprojects.com/en/7.x/options/#dynamic-defaults-for-prompts
@click.group()
def cli():
    pass

cli.add_command(record)
cli.add_command(domain)

if __name__ == '__main__':
    cli()
