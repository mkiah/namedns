import click

@click.group()
def domain():
    pass

@domain.command()
def list():
    raise NotImplementedError