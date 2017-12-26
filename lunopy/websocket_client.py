import asyncio
import websockets
from config import KEY, SECRET
import json

async def connect_websocket():

    api_key = {'api_key_id': KEY, 'api_key_secret': SECRET}
    message = json.dumps(api_key)

    async with websockets.connect('wss://ws.luno.com/api/1/stream/XBTZAR') as websocket:
        await websocket.send(message)

        response = await websocket.recv()
        decoded_response = json.loads(response)
        
        return decoded_response