#!/user/bin/env python
import ConfigParser
import json
import requests

from base64 import b64encode

#Load Settings
parser = ConfigParser.SafeConfigParser()
parser.read('config.ini')

LIP = parser.get('Login Parameters', 'LINK_IP')
LPT = parser.get('Login Parameters', 'LINK_PROTOCOL')

with open('red.json') as data_file:
   red = json.load(data_file)

with open('blue.json') as data_file:
   blue =json.load(data_file)

with open('green.json') as data_file:
   green=json.load(data_file)

with open('token.json') as data_file:
    data = json.load(data_file)

authheaders = { 'Authorization' : 'Bearer %s' %  data["session_token"] }
linkurl = LPT + "://" + LIP + ":3000"

with open('services.json') as data_file:
    services = json.load(data_file)

r=requests.put(linkurl+"/services/"+services[0]["id"]+"/state", headers=authheaders, json=red)
