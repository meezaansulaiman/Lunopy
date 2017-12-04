import websocket
import time
import config
from requests.auth import HTTPBasicAuth


def on_message(ws, message):
    print("messages")
    print(message)


def on_error(ws, error):
    print("error")
    print(error)


def on_close(ws):
    print("closed")


def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)

        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run,())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://ws.luno.com/api/1/stream/XBTZAR", 
        on_message=on_message, 
        on_error = on_error, 
        on_close=on_close,
        # header=['"api_key_id":"{}"'.format(config.KEY),'"api_key_secret":"{}"'.format(config.SECRET) ]
        header=['"{}"'.format(config.KEY), '"{}"'.format(config.SECRET)]
        )
    ws.on_open = on_open
    ws.run_forever()

