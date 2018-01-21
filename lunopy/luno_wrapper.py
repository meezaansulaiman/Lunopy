import requests
from requests.auth import HTTPBasicAuth
from . import build_api_call, build_query_string, connect_websocket
# from websocket_client import connect_websocket
import asyncio

class Luno:

    base_url = 'https://api.mybitx.com/api/1'

    def __init__(self, KEY, SECRET, ACCOUNTID):
        self.KEY = KEY
        self.SECRET = SECRET
        self.ACCOUNTID = ACCOUNTID

    # ---------------------------------------------------------------------------------------------------------------
    #    PENDING ORDERS
    # ---------------------------------------------------------------------------------------------------------------
    def get_pending_orders(self):
        """
        Gets pending orders placed
        :return: 
        """

        r = requests.get(build_api_call(self.base_url, self.ACCOUNTID, 'pending', ''), auth=HTTPBasicAuth(self.KEY, self.SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'

    # ---------------------------------------------------------------------------------------------------------------
    #    ORDERS
    # ---------------------------------------------------------------------------------------------------------------
    def get_list_orders(self, state=None, pair='XBTZAR'):
        """
        Gets list orders
        :return: 
        """
        data = {}
        if state is not None:
            data['state'] = state

        if pair is not None:
            data['pair'] = pair

        query_string = build_query_string(data)

        r = requests.get(build_api_call(self.base_url, None, 'listorders', query_string), auth=HTTPBasicAuth(self.KEY, self.SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'

    def post_limit_order(self, pair, type, volume, price, base_account_id=None, counter_account_id=None):
        """
        Create a new trade order.
        Warning! Orders cannot be reversed once they have executed. Please ensure your program has been thoroughly tested before submitting orders.
        If no base_account_id or counter_account_id are specified, your default base currency or counter currency account will be used. You can find your account IDs by calling the Balances API.
        """
        if pair is None:
            return "pair is None and is a required field"

        if type is None:
            return "type is None and is a required field"

        if volume is None:
            return "volume is None and is a required field"
        
        if price is None:
            return "price is None and is a required field"

        data = {
            'type': type,
            'volumne': volume,
            'price': price
        }

        if base_account_id is not None:
            data['base_account_id'] = base_account_id
        if counter_account_id is not None:
            data['counter_account_id'] = counter_account_id

        r = requests.post(build_api_call(self.base_url, None, 'postorder', ''),
                          data=data, auth=HTTPBasicAuth(self.KEY, self.SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'

    def post_market_order(self, type, counter, base_volume, base_account_id=None, counter_account_id=None):
        """
        A market order executes immediately, and either buys as much bitcoin that can be bought for a set amount of fiat currency, or sells a set amount of bitcoin for as much fiat as possible.
        
        :param type: string  required - "BUY" to buy bitcoin, or "SELL" to sell bitcoin.
        :param counter: string  required - if type is "BUY" For a "BUY" order: amount of local currency (e.g. ZAR, MYR) to spend as a decimal string in units of the local currency e.g. "100.50".
        :param base_volume: required - if type is "SELL"  For a "SELL" order: amount of Bitcoin to sell as a decimal string in units of BTC e.g. "1.423".
        :param base_account_id: string  optional - The base currency account to use in the trade.
        :param counter_account_id: string  optional - The counter currency account to use in the trade.
        :return: 
        """

        if type is None:
            return "Type is None and is a required field"

        if counter is None:
            return "Counter is None and is a required field"

        if base_volume is None:
            return "Base Volume is None and is a required field"

        data = {
            'type': type,
            'counter': counter,
            'base_volume': base_volume
        }

        if base_account_id is not None:
            data['base_account_id'] = base_account_id

        if counter_account_id is not None:
            data['counter_account_id'] = counter_account_id

        r = requests.post(build_api_call(self.base_url, None, 'marketorder', ''),
                          data=data, auth=HTTPBasicAuth(self.KEY, self.SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'

    def stop_order(self, order_id):
        """
        Request to stop an order.

        :param order_id: string - The order reference as a string e.g. BXMC2CJ7HNB88U4
        :return: 
        """

        data = {
            'order_id':order_id
        }

        r = requests.post(build_api_call(self.base_url, None, 'stoporder', ''),
                          data=data, auth=HTTPBasicAuth(self.KEY, self.SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'


    def get_order(self, order_id):
        """
        Get an order by its id.

        :param order_id: string - The order ID
        :return: 
        """
        data = {
            'order_id': order_id
        }

        r = requests.post(build_api_call(self.base_url, None, 'orders', ''),
                          data=data, auth=HTTPBasicAuth(self.KEY, self.SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'
    
