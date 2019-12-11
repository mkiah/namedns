from utils import namedns

namedotcom = namedns.Session('user', 'token', True)

namedotcom.list('pseudo.coffee')
