import requests

class Session():

    BASE_URL = 'api.name.com'
    BASE_DEV_URL = 'api.dev.name.com' 
    API_VERSION = '4'

    def __init__(self, username, api_token, dev=False):
        self.username = username if not dev else f"{username}-test"
        self.api_token = api_token
        self.base_url = self.BASE_URL if not dev else self.BASE_DEV_URL 

    def list(self, domain):
        """List all DNS records for the given domain.
        """
        r = requests.get(f"https://{self.base_url}/domains/{domain}/records")

        if not r.ok:
            r.raise_for_status()

        return r.json()
    

    def get(self, record_id):
        """Get details about a specific record by id.
        """
        pass
    

    def create(self, domain, host, record_type, answer, ttl=0, priority=None):
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
        pass
    

    def update(self, record_id, **kwargs):
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


    def __make_headers():
        """Generate HTTP headers.
        
        Returns
        -------
        dict,
            Headers for Name.com http requests
        """
        pass


