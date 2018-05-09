import requests
from requests.auth import HTTPBasicAuth
from . import build_api_call, build_query_string, connect_websocket
from .methods import Accounts, Orders, Prices, Trades, Transactions
# from websocket_client import connect_websocket
import asyncio

class Luno:

    def __init__(self, KEY, SECRET, ACCOUNTID):
        self.KEY = KEY
        self.SECRET = SECRET
        self.ACCOUNTID = ACCOUNTID
        
        self._accounts = None
        self._orders = None
        self._prices = None
        self._trades = None
        self._transactions = None

    @property
    def accounts(self):
        """
        Account related information
        :return:
        """
        if self._accounts is None:
            self._accounts = Accounts(self.KEY, self.SECRET, self.ACCOUNTID)

        return self._accounts

    @property
    def orders(self):
        if self._orders is None:
            self._orders = Orders(self.KEY, self.SECRET, self.ACCOUNTID)

        return self._orders

    @property
    def prices(self):
        if self._prices is None:
            self._prices = Prices(self.KEY, self.SECRET, self.ACCOUNTID)

        return self._prices

    @property
    def trades(self):
        if self._trades is None:
            self._trades = Trades(self.KEY, self.SECRET, self.ACCOUNTID)

        return self._trades

    @property
    def transactions(self):
        if self._transactions is None:
            self._transactions = Transactions(self.KEY, self.SECRET, self.ACCOUNTID)

        return self._transactions
