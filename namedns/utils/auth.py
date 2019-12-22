import click

# WARNING - currently only works if topmost decorator
def requires_auth(func):
    """Decorator for requiring auth.
    
    Adapted from https://github.com/pallets/click/issues/108#issuecomment-280489786
    """
    @click.option('--user', required=True)
    @click.option('--token', required=True)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
