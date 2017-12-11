import requests
from requests.auth import HTTPBasicAuth
from config import KEY, SECRET, ACCOUNTID
from utils.Helper import build_api_call, build_query_string


class Luno:

    base_url = 'https://api.mybitx.com/api/1/'

    def __init__(self):
        self.KEY = KEY
        self.SECRET = SECRET

    def get_price(self, pair='XBTZAR'):

        """
        Gets the price of bitcoin 
        :param pair: eg. XBTZAR
        :return: json
        """
        data = {'pair': pair}
        query_string = build_query_string(data)

        r = requests.get(build_api_call(self.base_url, None, 'ticker', query_string))
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
            r = requests.get(build_api_call(self.base_url, None, 'ticker', query_string))
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

        r = requests.get(build_api_call(self.base_url, None, 'orderbook', query_string))
        if r.status_code == 200:
            return r.json()
    
    def get_trades(self, pair='XBTZAR'):
        """
        Gets the recent trades per pair
        :param pair: eg. XBTZAR
        :return: 
        """
        data = {'pair': pair}
        query_string = build_query_string(data)

        r = requests.get(build_api_call(self.base_url, None, 'trades', query_string))
        if r.status_code == 200:
            return r.json()

    def get_balance(self):
        """
        Gets luno's account balance
        :return: 
        """
        r = requests.get(build_api_call(self.base_url, None, 'balance', ''), auth=HTTPBasicAuth(KEY, SECRET))
        if r.status_code == 200:
            return r.json()
        else:
            return 'error'

    def get_account_transactions(self, min_row=0, max_row=100):
        """
        Gets luno's account transactions
        :return: 
        """
        data = {
            'min_row': min_row,
            'max_row': max_row
        }
        query_string = build_query_string(data)

        r = requests.get(build_api_call(self.base_url, ACCOUNTID, 'transactions', query_string),
                         auth=HTTPBasicAuth(KEY, SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'

    # ---------------------------------------------------------------------------------------------------------------
    #    PENDING ORDERS
    # ---------------------------------------------------------------------------------------------------------------
    def get_pending_orders(self):
        """
        Gets pending orders placed
        :return: 
        """

        r = requests.get(build_api_call(self.base_url, ACCOUNTID, 'pending', ''), auth=HTTPBasicAuth(KEY, SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'

    # ---------------------------------------------------------------------------------------------------------------
    #    ORDERS
    # ---------------------------------------------------------------------------------------------------------------
    def get_list_orders(self, state=None, pair=None):
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

        r = requests.get(build_api_call(self.base_url, ACCOUNTID, 'listorders', query_string), auth=HTTPBasicAuth(KEY, SECRET))

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
                          data=data, auth=HTTPBasicAuth(KEY, SECRET))

        if r.status_code == 200:
            return r.json()
        else:
            return 'error'

