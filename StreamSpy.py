import requests
import time
import json
art = """                                                                                                                              
Discord Stream Spy by Professional
usage get stream url example:https://discordapp.com/api/v9/streams/guild%%3A1023413424350318642%%3A1023413427168870503%%3A899289008666976306/preview?version=
"""
print(art)
Token = input("Enter Token:")
URL = input("Stream URL:")
while True:

    headers ={
    "Authorization":f"{Token}",
    }

    url = f"{URL}{time.time()}"
    r = requests.Session()
    r = requests.get(f"{url}", headers =headers)
    data = json.loads(r.text)
    print(data['url'])
    time.sleep(300)
