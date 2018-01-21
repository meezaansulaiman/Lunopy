from config import BASEURL
import requests
from requests.auth import HTTPBasicAuth
from lunopy.utils import build_api_call, build_query_string, Helper
from lunopy.websocket_client import connect_websocket
import asyncio


class Transactions:
    def __init__(self, key, secret, accountid):
        self.KEY = key
        self.SECRET = secret
        self.ACCOUNTID = accountid

    def get_account_transactions(self, min_row=0, max_row=100):
        """
        Gets luno's account transactions
        
        :param min_row: 
        :param max_row: 
        :return: 
        """

        data = {
            'min_row': min_row,
            'max_row': max_row
        }
        query_string = build_query_string(data)
        url = build_api_call(base_url=BASEURL, account_id=self.ACCOUNTID, method='transactions', query_string=query_string)
        r = requests.get(url=url, auth=HTTPBasicAuth(self.KEY, self.SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'
