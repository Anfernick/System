import asyncio
import websockets

async def subscribe():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        print("Esperando mensajes...")
        async for message in websocket:
            print(f"Mensaje recibido: {message}")

# Iniciar el suscriptor
asyncio.get_event_loop().run_until_complete(subscribe())
