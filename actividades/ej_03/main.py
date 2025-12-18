import uasyncio as asyncio
from app import start_server, loop_sensor
import uasyncio as asyncio

async def main():
    # Crear tarea para actualizar sensor periódicamente
    asyncio.create_task(loop_sensor())
    # Iniciar servidor web
    start_server()

# Iniciar la aplicación
asyncio.run(main())