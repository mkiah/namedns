import argparse
from utils import namedns


def main():
    parser = argparse.ArgumentParser(description="Generate or renew letsencrypt \
        certificates and authenticate with name.com API")
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-u', '--username', dest='username', type=str, required=True, help='Name.com username.')
    required_args.add_argument('-t', '--api-token', dest='api_token', type=str, required=True, help='Name.com password.')
    parser.add_argument('-d', '--dev', dest='dev', action='store_true', help='Use the name.com dev server.')
    args = parser.parse_args()

    print('Ignoring --dev flag and hardcoding to user dev server for testing.')
    namedotcom = namedns.Session(args.username, args.api_token, True) #Forced to use DEV environment while testing
    namedotcom.list('pseudo.coffee')

if __name__ == '__main__':
    main()