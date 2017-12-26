from . import Luno

if __name__ == "__main__":
    l = Luno()

    while True:
        # asks = []
        response = l.get_ws_price()
        asks = response['asks']
        print(asks)
    # print(l.get_pending_orders())
    # print(l.get_account_transactions())

