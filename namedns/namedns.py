import requests

class Session():

    API_VERSION = '4'
    BASE_URL = 'https://api.name.com'
    BASE_DEV_URL = 'https://api.dev.name.com'

    def __init__(self, username, api_token, dev=False):
        self.username = username if not dev else f"{username}-test"
        self.api_token = api_token
        self.auth = (self.username, self.api_token)
        base_url = self.BASE_URL if not dev else self.BASE_DEV_URL
        self.base_url = f"{base_url}/v{self.API_VERSION}"


    def list_domains(self):
        """List all domains for the given account.

        Returns
        -------
        list,
            list of domains associated with the account.
        """
        url = f"{self.base_url}/domains"
        r = requests.get(url, auth=(self.username, self.api_token))

        if not r.ok:
            print(r.content)
            r.raise_for_status()
        
        return r.json()['domains']


    def get_domain(self, domain):
        """Get details about a specific domain.

        Parameters
        ----------
        domain, str
            domain to get details about.
        
        Returns
        -------
        dict,
            details about the provided domain.
        """
        url = f"{self.base_url}/domains/{domain}"
        r = requests.get(url, auth=self.auth)

        if not r.ok:
            print(r.content)
            r.raise_for_status()
        
        return r.json()


    def list_records(self, domain):
        """List all DNS records for the given domain.

        Returns
        -------
        """
        url = f"{self.base_url}/domains/{domain}/records"
        r = requests.get(url, auth=(self.username, self.api_token))

        if not r.ok:
            print(r.content)
            r.raise_for_status()

        return r.json()['records']
    

    def get_record(self, record_id):
        """Get details about a specific record by id.
        """
        pass
    

    def create_record(self, domain, host, record_type, answer, ttl=3600, priority=None):
        """Create a new DNS record.
    
        Parameters
        ----------
        domain, str
            domain zone to create a record for (e.g. example.org)
        host, str
            hostname relative to the zone (e.g., www for www.example.org)
        record_type, str {A, AAAA, ANAME, CNAME, MX, NS, SRV, TXT}
            type of record to be created
        answer, str
            Answer is either the IP address for A or AAAA records; the target for 
            ANAME, CNAME, MX, or NS records; the text for TXT records. 
        ttl, uint32 (optional)
            the time in seconds that this record should be cached (minimum 300s)
        """
        if answer.lower() in ['MX', 'SRV']:
            raise NotImplementedError
        
        if ttl < 300:
            raise ValueError(f'Minimum ttl value is 300.')

        url = f'{self.base_url}/domains/{domain}/records'
        payload = {
            'host': host,
            'type': record_type,
            'ttl': ttl,
            'answer': answer
        }
        if priority:
            data['priority'] = priority
        
        r = requests.post(url, auth=self.auth, json=payload)
        if not r.ok:
            print(r.content)
            r.raise_for_status()

        return r.json()

    def update_record(self, record_id, **kwargs):
        """Update an existing DNS record.
    
        Parameters
        ----------
        record_id, int
            the unique ID of the record to be updated.
        domain, str
            domain zone to create a record for (e.g. example.org)
        host, str
            hostname relative to the zone (e.g., www for www.example.org)
        record_type, str {A, AAAA, ANAME, CNAME, MX, NS, SRV, TXT}
            type of record to be created
        answer, str
            Answer is either the IP address for A or AAAA records; the target for 
            ANAME, CNAME, MX, or NS records; the text for TXT records. 
        ttl, uint32 (optional)
            the time in seconds that this record should be cached (minimum 300s)
        
        """
        pass

    
    def delete_record(self, domain, record_id):
        """Delete the given DNS record.

        Parameters
        ----------
        domain, str
            the domain to delete the record from.
        record_id, int
            the unique dns record id to delete.
        """
        url = f"{self.base_url}/domains/{domain}/records/{record_id}"
        r = requests.delete(url, auth=self.auth)

        if not r.ok:
            print(r.content)
            r.raise_for_status()

        return r.json()
