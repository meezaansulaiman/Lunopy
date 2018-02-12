from . import BASEURL
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

        r = requests.get(build_api_call(BASEURL, None, 'trades', query_string), auth=HTTPBasicAuth(self.KEY, self.SECRET))
        if r.status_code == 200:
            return r.json()

    def get_fee_information(self):
        """
        Fee Information

        Returns your fees and 30 day trading volume (as of midnight) for a given pair.
        """
        url = build_api_call(base_url=self.base_url, account_id=None, method='fee_info', query_string=None)
        r = requests.get(url)

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'