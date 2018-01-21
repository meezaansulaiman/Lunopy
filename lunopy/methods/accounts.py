from config import BASEURL
import requests
from requests.auth import HTTPBasicAuth
from lunopy.utils import build_api_call, build_query_string, Helper
from lunopy.websocket_client import connect_websocket
import asyncio


class Accounts:
    def __init__(self, key, secret, accountid):
        self.KEY = key
        self.SECRET = secret
        self.ACCOUNTID = accountid
    
    def get_balance(self):
        """
        Gets luno's account balance
        :return: 
        """
        url = build_api_call(base_url=BASEURL, account_id=None, method='balance', query_string=None)
        r = requests.get(url=url, auth=HTTPBasicAuth(self.KEY, self.SECRET))
        if r.status_code == 200:
            return r.json()
        else:
            return 'error'
