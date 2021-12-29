import asyncio
import time


async def message1():
    while True:
        await asyncio.sleep(1)
        print("Running...")


async def message2():
    while True:
        await asyncio.sleep(5)
        print("Hello...")


loop = asyncio.get_event_loop()
loop.create_task(message1())
loop.create_task(message2())
loop.run_forever()

