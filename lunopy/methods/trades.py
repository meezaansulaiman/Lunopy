from config import BASEURL
import requests
from requests.auth import HTTPBasicAuth
from lunopy.utils import build_api_call, build_query_string, Helper
from lunopy.websocket_client import connect_websocket
import asyncio


class Trades:
    def __init__(self, key, secret, accountid):
        self.KEY = key
        self.SECRET = secret
        self.ACCOUNTID = accountid

    def get_trades(self, pair='XBTZAR'):
        """
        Gets the recent trades per pair
        :param pair: eg. XBTZAR
        :return: 
        """
        data = {'pair': pair}
        query_string = build_query_string(data)

        r = requests.get(build_api_call(BASEURL, None, 'trades', query_string))
        if r.status_code == 200:
            return r.json()