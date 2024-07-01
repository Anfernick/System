import asyncio
import websockets

async def publish_message(message):
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        print(f"Mensaje publicado: {message}")

# Publicar un mensaje
message = input("Ingrese el mensaje a publicar: ")
asyncio.get_event_loop().run_until_complete(publish_message(message))
