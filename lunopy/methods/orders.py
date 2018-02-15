from . import BASEURL
import requests
from requests.auth import HTTPBasicAuth
from lunopy.utils import build_api_call, build_query_string, Helper
from lunopy.websocket_client import connect_websocket
import asyncio

class Orders:
    def __init__(self, key, secret, accountid):
        self.KEY = key
        self.SECRET = secret
        self.ACCOUNTID = accountid

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

        r = requests.get(build_api_call(BASEURL, None, 'listorders', query_string), auth=HTTPBasicAuth(self.KEY, self.SECRET))

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

        r = requests.post(build_api_call(BASEURL, None, 'postorder', ''),
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

        r = requests.post(build_api_call(BASEURL, None, 'marketorder', ''),
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

        r = requests.post(build_api_call(BASEURL, None, 'stoporder', ''),
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

        r = requests.post(build_api_call(BASEURL, None, 'orders', ''),
                          data=data, auth=HTTPBasicAuth(self.KEY, self.SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'
    
    def list_trades(self, pair='XBTZAR', since=None, limit=None):
        """
        Returns a list of your recent trades for a given pair, sorted by oldest first.
        type in the response indicates the type of order that you placed in order to participate in the trade. Possible types: BID, ASK.
        If is_buy in the response is true, then the order which completed the trade (market taker) was a bid order.
        Results of this query may lag behind the latest data.


        
        Keyword Arguments:
            pair	string	required	Filter to trades of this currency pair e.g. XBTZAR
            since	integer	optional	Filter to trades on or after this timestamp, e.g. 1470810728478
            limit	integer	optional	Limit to this number of trades (min 1, max 100, default 100)

        """

        data = {
            'pair':pair
        }

        if since is not None:
            data.update({'since':since})
        
        if limit is not None:
            data.update({'limit':limit})

        query_string = build_query_string(query_obj=data)
        url = build_api_call(base_url=self.base_ur, account_id=None, method='listtrades',query_string=query_string)
        r = requests.get(url)

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'