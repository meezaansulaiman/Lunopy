from config import BASEURL
import requests
from requests.auth import HTTPBasicAuth
from lunopy.utils import build_api_call, build_query_string, Helper
from lunopy.websocket_client import connect_websocket
import asyncio


class Prices:

    def __init__(self, key, secret, accountid):
        self.KEY = key
        self.SECRET = secret
        self.ACCOUNTID = accountid

    def get_ws_price(self, pair='XBTZAR'):
        """
        Gets the prices via websockets
        :param pair: string - eg. XBTZAR
        """
        return asyncio.get_event_loop()\
            .run_until_complete(connect_websocket(KEY=self.KEY, SECRET=self.SECRET))

    def get_price(self, pair='XBTZAR'):
        """
        Gets the price of bitcoin 
        :param pair: eg. XBTZAR
        :return: json
        """
        data = {'pair': pair}
        query_string = build_query_string(data)

        url = build_api_call(base_url=BASEURL, account_id=None, method='ticker', query_string=query_string)
        r = requests.get(url=url)
        if r.status_code == 200:
            return r.json()

    def get_rolling_price(self, pair='XBTZAR'):
        """
        Gets the rolling price of bitcoin 
        :param pair: eg. XBTZAR
        :return: json
        """

        data = {'pair': pair}
        query_string = build_query_string(data)

        while True:
            url = build_api_call(base_url=BASEURL, account_id=None, method='ticker', query_string=query_string)
            r = requests.get(url=url)
            if r.status_code == 200:
                print(r.json())

    def get_orderbook(self, pair='XBTZAR'):
        """
        Gets the orderbook of bitcoin 
        :param pair: eg. XBTZAR
        :return: json
        """

        data = {'pair': pair}
        query_string = build_query_string(data)
        url = build_api_call(base_url=BASEURL, account_id=None, method='orderbook', query_string=query_string)
        r = requests.get(url=url)
        if r.status_code == 200:
            return r.json()

