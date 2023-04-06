import asyncio


async def my_coroutine() -> None:
    print('Hello World!')


asyncio.run(my_coroutine())