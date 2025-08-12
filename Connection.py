'''
This "Connection" Object will act as the main object facilitating the connection to
the Destiny 2 API. This object must be initialized in order to utilize anything in
this library.
'''
import os
import requests
from time import sleep

class Connection(object):
    sleeptime= .1
    APIKey= ''

    def __init__(self):
        self.APIKey= os.environ.get("BungieAPIKey")

    '''
    This is the most general call possible
    '''
    def baseCall(self, call_argument):
        siteCall= "https://www.bungie.net/Platform/Destiny2" + str(call_argument)
        try:
            response= requests.get(siteCall, headers= {"X-API_KEY": self.APIKey})
            sleep(self.sleeptime)
            if response.status_code == 200:
                return response.json()
            else:
                return "Response clear : Bad Status : " + str(response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")

