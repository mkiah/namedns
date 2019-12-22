import click
from namedns import namedns
from namedns import utils

@click.group()
def record():
    pass


@record.command()
@click.option('--ttl', default=3600, type=int, help='TTL is the time this record can be cached for in seconds. Minimum of 300 seconds')
@click.option('--priority', help="Priority is only required for MX and SRV records, it is ignored for all others.")
@click.option('--type', 'record_type', required=True, type=click.Choice(['A', 'AAAA', 'ANAME', 'CNAME', 'MX', 'NS', 'SRV', 'TXT'], case_sensitive=False))
@click.option('--host', required=True, type=str)
@click.option('--answer', required=True, type=str)
@click.option('--domain', required=True, type=str)
@click.option('--user', prompt='Username.', required=True)
@click.option('--token', prompt='API Token.', hide_input=True, required=True)
def add(user, token, record_type, host, domain, answer, ttl, priority=None):
    """Add DNS record.

    record_type  the type of DNS record to create.

    host  the hostname relative to the domain (e.g., blog for blog.example.com)

    answer  is either the IP address for A or AAAA records; the target for ANAME, CNAME, MX, or NS records; the text for TXT records. For SRV records, answer has the following format: '<weight> <port> <target>' (e.g. '1 5061 sip.example.org')
    """
    session = namedns.Session(user, token)
    # return session.create_record(domain=domain, host=host, record_type=record_type, ttl=ttl, answer=answer, priority=priority)
    click.echo(
        f"domain={domain}, host={host}, record_type={record_type}, ttl={ttl}, answer={answer}, priority={priority}")


@record.command()
@click.option('--host')
@click.option('--type')
# @click.argument('test')
def remove(test):
    """Remove a record."""
    pass
