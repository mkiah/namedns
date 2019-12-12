import argparse
import pprint
import sys
from utils import namedns


def main():
    parser = argparse.ArgumentParser(description="Generate or renew letsencrypt \
        certificates and authenticate with name.com API")
    required = parser.add_argument_group('required arguments')
    required.add_argument('-u', '--username', dest='username', type=str, 
        required=True, help='Name.com username.')
    required.add_argument('-a', '--api-token', dest='api_token', type=str, 
        required=True, help='Name.com password.')
    required.add_argument('-d', '--domain', dest='domain', type=str, help='The domain to take action on.')

    create = parser.add_argument_group('create records')
    create.add_argument('--host', dest='host', type=str, 
        help='Hostname relative to the domain (e.g., blog for blog.example.com)')
    create.add_argument('--type', dest='type', type=str, choices=['A', 'AAAA', 'ANAME', 'CNAME', 'MX', 'NS', 'SRV', 'TXT'])
    create.add_argument('--answer', dest='answer', type=str, 
        help="Answer is either the IP address for A or AAAA records; the \
            target for ANAME, CNAME, MX, or NS records; the text for TXT \
            records. For SRV records, answer has the following format: \
            '<weight> <port> <target>' (e.g. '1 5061 sip.example.org')")
    create.add_argument('--ttl', dest='ttl', default=3600, type=int, 
        help="TTL is the time this record can be cached for in seconds. Minimum of 300 seconds")
    create.add_argument('--priority', dest='priority', type=int, 
        help="Priority is only required for MX and SRV records, it is ignored for all others.")

    parser.add_argument('--dev', "--test", dest='dev', action='store_true', help='Use the name.com dev server.')
    args = parser.parse_args()
    if args.ttl and args.ttl < 300:
        parser.error(f'Time to live (TTL) value of {args.ttl} invalid. Minimum value is 300.')

    namedotcom = namedns.Session(args.username, args.api_token, args.dev) 
    
    records = namedotcom.list_records(args.domain)
    txt_records = []
    for record in records:
        if f'_acme-challenge.{args.domain}' in record['fqdn']:
            txt_records.append(record)
    print(txt_records)

    if not txt_records:
        new_record = namedotcom.create_record(
            domain=args.domain,
            host='_acme-challenge',
            record_type='TXT',
            ttl=300,
            answer='1234')
        pprint.pprint(new_record)



if __name__ == '__main__':
    main()