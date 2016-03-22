# hue_scripts
# setup
You will need to have a config.ini which has the parameters as follows:
<pre>
[Login Parameters]
AUTH_CODE:<authcode in base 64>
LINK_IP:<ip address of your foxbox>
LINK_PROTOCOL:<http or https>
</pre>
#Scripts : 
* python login.py : to authenticate
* python services.py : gives a services.json; need to run at least once
* python devicestate.py : gives a devicestate.json
* python red_light.py : changes the light to red
* python green_light.py : changes the light to green
* python blue_light.py : changes the light to blue
* python pulse.py : pulses the light

#To Do:
Need to refactor and make into various functions and such.
