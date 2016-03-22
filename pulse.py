#!/user/bin/env python
import time
import ConfigParser
import json
import requests

from base64 import b64encode

#Load Settings
parser = ConfigParser.SafeConfigParser()
parser.read('config.ini')

LIP = parser.get('Login Parameters', 'LINK_IP')
LPT = parser.get('Login Parameters', 'LINK_PROTOCOL')

with open('pulse_up.json') as data_file:
   pulse_up = json.load(data_file)

with open('pulse_mid.json') as data_file:
   pulse_mid =json.load(data_file)

with open('pulse_down.json') as data_file:
   pulse_down=json.load(data_file)

with open('token.json') as data_file:
    data = json.load(data_file)

authheaders = { 'Authorization' : 'Bearer %s' %  data["session_token"] }
linkurl = LPT + "://" + LIP + ":3000"

with open('services.json') as data_file:
    services = json.load(data_file)

while True:
    r=requests.put(linkurl+"/services/"+services[0]["id"]+"/state", headers=authheaders, json=pulse_up)
    time.sleep (0.1)
    r=requests.put(linkurl+"/services/"+services[0]["id"]+"/state", headers=authheaders, json=pulse_mid)
    time.sleep(0.1)
    r=requests.put(linkurl+"/services/"+services[0]["id"]+"/state", headers=authheaders, json=pulse_down)
    time.sleep(0.1)
    r=requests.put(linkurl+"/services/"+services[0]["id"]+"/state", headers=authheaders, json=pulse_mid)
