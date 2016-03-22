#!/user/bin/env python
import ConfigParser
import json
import requests

from base64 import b64encode

#Load Settings
parser = ConfigParser.SafeConfigParser()
parser.read('config.ini')

UID = parser.get('Login Parameters', 'AUTH_CODE')
LIP = parser.get('Login Parameters', 'LINK_IP')
LPT = parser.get('Login Parameters', 'LINK_PROTOCOL')

# username = parser.get('Login Parameters', 'USERNAME')
# username = parser.get('Login Parameters', 'PASSWORD')
# UID = b64encode(b"username:password").decode("ascii")
authheaders = { 'Authorization' : 'Basic %s' %  UID }

linkurl = LPT + "://" + LIP + ":3000"

linkservices = '/services/list'
linklogin = "/users/login"

r=requests.post(linkurl+linklogin, headers=authheaders)
data=r.json()

f = open ('token.json', 'w')
json.dump(data, f)
