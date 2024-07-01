import asyncio
import websockets
import threading

# Servidor WebSocket
async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        connected_clients.remove(websocket)

def start_server():
    start_server = websockets.serve(handler, "localhost", 6789)
    asyncio.get_event_loop().run_until_complete(start_server)
    print("Servidor WebSocket iniciado en ws://localhost:6789")
    asyncio.get_event_loop().run_forever()

# Publicador
async def publish_message(message):
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        print(f"Mensaje publicado: {message}")

def start_publisher():
    message = input("Ingrese el mensaje a publicar: ")
    asyncio.get_event_loop().run_until_complete(publish_message(message))

# Suscriptor
async def subscribe():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        print("Esperando mensajes...")
        async for message in websocket:
            print(f"Mensaje recibido: {message}")

def start_subscriber():
    asyncio.get_event_loop().run_until_complete(subscribe())

# Conjunto de clientes conectados
connected_clients = set()

# Iniciar servidor en un hilo separado
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Esperar un momento para que el servidor inicie
import time
time.sleep(1)

# Iniciar publicador en un hilo separado
publisher_thread = threading.Thread(target=start_publisher)
publisher_thread.start()

# Iniciar suscriptor en un hilo separado
subscriber_thread = threading.Thread(target=start_subscriber)
subscriber_thread.start()
