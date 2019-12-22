import click

@click.group()
def record():
    pass

@record.command()
@click.option('--ttl', default=3600, type=int, help='TTL is the time this record can be cached for in seconds. Minimum of 300 seconds')
@click.option('--priority', help="Priority is only required for MX and SRV records, it is ignored for all others.")
@click.argument('host', type=str)
@click.argument('record_type', type=click.Choice(['A', 'AAAA', 'ANAME', 'CNAME', 'MX', 'NS', 'SRV', 'TXT'], case_sensitive=False))
@click.argument('answer', type=str)
def add(session, domain, host, record_type, ttl, answer, priority=None):
    """Add DNS record.

    host  the hostname relative to the domain (e.g., blog for blog.example.com)
    
    record_type  the type of DNS record to create.

    answer  is either the IP address for A or AAAA records; the target for ANAME, CNAME, MX, or NS records; the text for TXT records. For SRV records, answer has the following format: '<weight> <port> <target>' (e.g. '1 5061 sip.example.org')
    """
    return session.create_record(domain=domain, host=host, record_type=record_type, ttl=ttl, answer=answer, priority=priority)


@record.command()
@click.option('--host')
@click.option('--type')
# @click.argument('test')
def remove(test):
    """Remove a record."""
    pass
