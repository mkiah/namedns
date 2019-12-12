import argparse
import pprint
from utils import namedns


def main():
    parser = argparse.ArgumentParser(description="Generate or renew letsencrypt \
        certificates and authenticate with name.com API")
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-u', '--username', dest='username', type=str, required=True, help='Name.com username.')
    required_args.add_argument('-t', '--api-token', dest='api_token', type=str, required=True, help='Name.com password.')
    required_args.add_argument('-d', '--domain', dest='domain', type=str, required=True, help='The domain to take action on.')
    parser.add_argument('--dev', "--test", dest='dev', action='store_true', help='Use the name.com dev server.')
    args = parser.parse_args()

    print('Ignoring --dev flag and hardcoding to user dev server for testing.')
    namedotcom = namedns.Session(args.username, args.api_token, True) #Forced to use DEV environment while testing
    pprint.pprint(namedotcom.list_domains())

if __name__ == '__main__':

    main()