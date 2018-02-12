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
        
        self.accounts = None
        self.orders = None
        self.prices = None
        self.trades = None
        self.transactions = None
    

    def accounts(self):
        if self.accounts is None:
            self.accounts = Accounts(self.KEY, self.SECRET, self.ACCOUNTID)

        return self.accounts

    def orders(self):
        if self.orders is None:
            self.orders = Orders(self.KEY, self.SECRET, self.ACCOUNTID)

        return self.orders

    def prices(self):
        if self.prices is None:
            self.prices = Prices(self.KEY, self.SECRET, self.ACCOUNTID)

        return self.prices

    def trades(self):
        if self.trades is None:
            self.trades = Trades(self.KEY, self.SECRET, self.ACCOUNTID)

        return self.trades

    def transactions(self):
        if self.transactions is None:
            self.transactions = Transactions(self.KEY, self.SECRET, self.ACCOUNTID)

        return self.transactions
    