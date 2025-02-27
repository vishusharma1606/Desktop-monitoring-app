import asyncio
import json
import websockets
import psutil

# WebSocket server settings
HOST = 'localhost'
PORT = 8081  # Updated port

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

async def monitor_system(websocket):  # ✅ Fix: Removed extra parameter
    try:
        while True:
            ram_usage = get_ram_usage()
            disk_usage = get_disk_usage()
            
            alert = None
            if ram_usage > 80:
                alert = f'RAM usage critical: {ram_usage:.2f}%'
            elif ram_usage >= 60:
                alert = f'RAM usage high: {ram_usage:.2f}%'
            
            data = {
                'ram_usage': ram_usage,
                'disk_usage': disk_usage,
                'alert': alert
            }
            
            await websocket.send(json.dumps(data))
            await asyncio.sleep(2)  # Send updates every 2 seconds
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    async with websockets.serve(monitor_system, HOST, PORT):  # ✅ Fix: Corrected function call
        print(f'WebSocket server running on ws://{HOST}:{PORT}')
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Server stopped by user")
