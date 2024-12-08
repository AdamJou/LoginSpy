import asyncio
import websockets
import platform
from datetime import datetime

async def send_log():
    # Adres serwera WebSocket (zastąp własnym adresem z Render)
    uri = "wss://websocket-server.onrender.com/ws"
    computer_name = platform.node()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        async with websockets.connect(uri) as websocket:
            message = f"Computer '{computer_name}' started at {current_time}"
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Server response: {response}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(send_log())
