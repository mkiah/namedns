import click


@click.group(help='Manage domains.')
def domain():
    pass

@domain.command()
def list():
    raise NotImplementedError
