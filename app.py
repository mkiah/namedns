import argparse
import pprint
import sys
from utils import namedns


def add_record(domain, host, record_type, ttl, answer, priority=None):
    return namedotcom.create_record(domain=domain, host=host, record_type=record_type, ttl=ttl, answer=answer, priority=priority)


def remove_record(domain, record_id):
    return namedotcom.delete_record(domain=domain, record_id=record_id)


parser = argparse.ArgumentParser(description="Generate or renew letsencrypt \
                                 certificates and authenticate with name.com API")
required = parser.add_argument_group('required arguments')
required.add_argument('-u', '--username', dest='username',
                      type=str, required=True, help='Name.com username.')
required.add_argument('-a', '--api-token', dest='api_token',
                      type=str, required=True, help='Name.com password.')
required.add_argument('-d', '--domain', dest='domain',
                      type=str, help='The domain to take action on.')

manage = parser.add_argument_group('manage records')
manage.add_argument('--record', dest='record',
                    type=str, choices=['add', 'remove'])
manage.add_argument('--host', dest='host', type=str,
                    help='Hostname relative to the domain (e.g., blog for blog.example.com)')
manage.add_argument('--type', dest='type', type=str, required=True,
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

parser.add_argument('--dev', "--test", dest='dev',
                    action='store_true', help='Use the name.com dev server.')
args = parser.parse_args()
if args.ttl and args.ttl < 300:
    parser.error(
        f'Time to live (TTL) value of {args.ttl} invalid. Minimum value is 300.')

namedotcom = namedns.Session(args.username, args.api_token, args.dev)

if args.record == 'add':
    record = add_record(domain=args.domain, host=args.host,
                        record_type=args.type, ttl=300, answer=args.answer)
    pprint.pprint(record)
elif args.record == 'remove':
    # raise NotImplementedError

    records = namedotcom.list_records(args.domain)
    # pprint.pprint(records)
    changed_records = []
    for record in records:
        # print(record['fqdn'].lower(), f'{args.host}.{args.domain}')
        if record['type'].lower() == args.type.lower() and record['fqdn'] == f'{args.host}.{args.domain}.':
            removed = remove_record(domain=args.domain, record_id=record['id'])
            changed_records.append(removed)
    print(f'Removed {len(changed_records)} records from {args.domain}.')
    pprint.pprint(changed_records)
