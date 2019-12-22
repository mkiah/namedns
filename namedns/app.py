import argparse
import pprint
import sys
import getpass
import textwrap
import click
from utils import namedns

# class NameDNS():
#     def __init__(self):
#         parser = argparse.ArgumentParser(
#             description="View or edit domains or domain DNS records using the Name.com rest API.",
#             usage='namedns <command> [<args>]',
#             formatter_class=argparse.RawDescriptionHelpFormatter,
#             epilog=textwrap.dedent("""\
#                 commands:
#                   record
#                 """))
#         # parser.add_argument('command', help='Command to run.')
#         parser.add_argument('--user')
#         parser.add_argument('--token')

#         subparsers = parser.add_subparsers(dest='command')
#         record_parser = subparsers.add_parser('record')
        
#         record_subparser = subparsers.add_subparsers(dest='record_command')
#         record_add_parser = record_subparser.add_parser('add')
#         record_add_parser.add_argument('host', type=str,
#                             help='Hostname relative to the domain (e.g., blog for blog.example.com)')
#         record_add_parser.add_argument('type', type=str.upper,
#                             choices=['A', 'AAAA', 'ANAME', 'CNAME', 'MX', 'NS', 'SRV', 'TXT'])
#         record_add_parser.add_argument('answer', type=str, help="Answer is either the IP address for A or AAAA records; the target   \
#             for ANAME, CNAME, MX, or NS records the text for TXTrecords. For SRV \
#             records, answer has the following format: '<weight> <port> <target>' \
#             (e.g. '1 5061 sip.example.org')")
#         record_add_parser.add_argument('--ttl', dest='ttl', default=3600, type=int,
#                             help="TTL is the time this record can be cached for in seconds. Minimum of 300 seconds"
#                             )
#         record_add_parser.add_argument('--priority', dest='priority', type=int,
#                             help="Priority is only required for MX and SRV records, it is ignored for all others.")

#         args = parser.parse_args()

#         if not hasattr(self, args.command):
#             print('Unrecognized command')
#             parser.print_help()
#             exit(1)

#         getattr(self, args.command)()


#     # def new_session(self):
#     #     """Create new name.com API session.
#     #     """
#     #     user = None
#     #     api_token = None
#     #     dev_server = False if '--dev' not in sys.argv else True

#     #     for index, arg in enumerate(sys.argv):
#     #         if arg == '--user':
#     #             user = sys.argv.pop(index+1)
#     #             sys.argv.pop(index)
#     #         if arg == '--token':
#     #             api_token = sys.argv.pop(index+1)
#     #             sys.argv.pop(index)

#     #     return namedns.Session(username=user, api_token=api_token, dev=dev_server)


#     def record(self):
#         """Manage DNS records for a given domain.
#         """
#         parser = argparse.ArgumentParser(
#             description='DNS operations on a given domain.',
#             formatter_class=argparse.RawDescriptionHelpFormatter,
#             epilog=textwrap.dedent("""\
#                 commands:
#                   add
#                   remove
#                   list
#                 """))
#         parser.add_argument('command', help='DNS command to run')
#         args = parser.parse_args(sys.argv[2:3])

#         getattr(self, f'record_{args.command}')()

#     def record_add(self):
#         """Add DNS record with the given attributes.
#         """
#         parser = argparse.ArgumentParser(
#             description='Add a DNS record to a given domain'
#         )
#         parser.add_argument('host', type=str,
#             help='Hostname relative to the domain (e.g., blog for blog.example.com)')
#         parser.add_argument('type', type=str.upper,
#             choices=['A', 'AAAA', 'ANAME', 'CNAME', 'MX', 'NS', 'SRV', 'TXT'])
#         parser.add_argument('answer', type=str, help=
#             "Answer is either the IP address for A or AAAA records; the target   \
#             for ANAME, CNAME, MX, or NS records the text for TXTrecords. For SRV \
#             records, answer has the following format: '<weight> <port> <target>' \
#             (e.g. '1 5061 sip.example.org')")
#         parser.add_argument('--ttl', dest='ttl', default=3600, type=int, 
#             help="TTL is the time this record can be cached for in seconds. Minimum of 300 seconds"
#         )
#         parser.add_argument('--priority', dest='priority', type=int,
#             help="Priority is only required for MX and SRV records, it is ignored for all others.")
#         args = parser.parse_args(sys.argv[3:])
#         print(f'Running namedns add-record {args.host} {args.type} {args.answer}')

#         # return self.session.create_record(domain=args.domain, host=args.host, record_type=args.type, ttl=args.ttl, answer=args.answer)

#     def record_remove(self):
#         """Remove DNS record.
#         """
#         raise NotImplementedError

#     def record_list(self):
#         """List DNS records for the given domain.
#         """
#         parser = argparse.ArgumentParser(
#             description="List DNS records for the given domain."
#         )
#         parser.add_argument('--type', dest='type', type=str.upper,
#             choices=['A', 'AAAA', 'ANAME', 'CNAME', 'MX', 'NS', 'SRV', 'TXT'],
#             help='List records with the given record type.')
#         parser.add_argument('--host', dest='host', type=str,
#             help='List records with the given host value.')
        
#         raise NotImplementedError


def main():
    parser = argparse.ArgumentParser(description="Generate or renew letsencrypt \
                                    certificates and authenticate with name.com API")
    parser.add_argument('--user', dest='username', type=str, help='API username.')
    parser.add_argument('--token', dest='api_token', type=str, help='API auth token.')
    parser.add_argument('--domain', dest='domain', type=str, help='The domain to take action on.')
    parser.add_argument('--dev', "--test", dest='dev',
                        action='store_true', help='Use the name.com dev server.')

    manage = parser.add_argument_group('manage records')
    manage.add_argument('--record', dest='record',
                        type=str, choices=['add', 'remove'])
    manage.add_argument('--host', dest='host', type=str,
                        help='Hostname relative to the domain (e.g., blog for blog.example.com)')
    manage.add_argument('--type', dest='type', type=str,
                        choices=['A', 'AAAA', 'ANAME', 'CNAME', 'MX', 'NS', 'SRV', 'TXT'])
    manage.add_argument('--answer', dest='answer', type=str,
                        help="Answer is either the IP address for A or AAAA records; the \
                        target for ANAME, CNAME, MX, or NS records; the text for TXT \
                        records. For SRV records, answer has the following format: \
                        '<weight> <port> <target>' (e.g. '1 5061 sip.example.org')")
    manage.add_argument('--ttl', dest='ttl', default=3600, type=int,
                        help="TTL is the time this record can be cached for in seconds. Minimum of 300 seconds")
    manage.add_argument('--priority', dest='priority', type=int,
                        help="Priority is only required for MX and SRV records, it is ignored for all others.")
    args = parser.parse_args()

    args.username = args.username if args.username else input('Username: ')
    args.api_token = args.api_token if args.api_token else getpass.getpass()

    namedotcom = namedns.Session(args.username, args.api_token, args.dev)

    if args.record == 'add':
        if not (args.type and args.host and args.answer):
            parser.error(f'Requires --type, --host, and --answer.')

        if args.ttl and args.ttl < 300:
            parser.error(
                f'Time to live (TTL) value of {args.ttl} invalid. Minimum value is 300.')

        record = add_record(session=namedotcom, domain=args.domain, host=args.host,
                            record_type=args.type, ttl=300, answer=args.answer)
        pprint.pprint(record)
    elif args.record == 'remove':
        if not (args.type and args.host):
            parser.error(f'Requires --type and --host.')

        records = namedotcom.list_records(args.domain)
        # pprint.pprint(records)
        changed_records = []
        for record in records:
            # print(record['fqdn'].lower(), f'{args.host}.{args.domain}')
            if record['type'].lower() == args.type.lower() and record['fqdn'] == f'{args.host}.{args.domain}.':
                removed = remove_record(session=namedotcom, domain=args.domain, record_id=record['id'])
                changed_records.append(removed)
        print(f'Removed {len(changed_records)} records from {args.domain}.')
        pprint.pprint(changed_records)
    elif args.domain:
        pprint.pprint(namedotcom.get_domain(args.domain))
    else:
        print(f'No tasks specified. Fetching list of associated domains.')
        pprint.pprint(namedotcom.list_domains())

@click.group()
def records():
    pass

@click.command()
@click.option('--ttl', default=3600, help='TTL is the time this record can be cached for in seconds. Minimum of 300 seconds')
# @click.option('--priority', help="Priority is only required for MX and SRV records, it is ignored for all others.")
@click.argument('host', type=str)
@click.argument('record_type', type=click.Choice(['A', 'AAAA', 'ANAME', 'CNAME', 'MX', 'NS', 'SRV', 'TXT']))
@click.argument('answer')
def add_record(record_host, record_type, answer, ttl):
    # return session.create_record(domain=domain, host=host, record_type=record_type, ttl=ttl, answer=answer, priority=priority)
    pass


def remove_record(session, domain, record_id):
    return session.delete_record(domain=domain, record_id=record_id)


if __name__ == "__main__":
    # NameDNS()
    click.argument(add_record)
