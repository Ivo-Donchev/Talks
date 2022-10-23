import asyncio

async def coroutine_func():
    pass

async def main():
    await coroutine_func()

if __name__ == '__main__':
    asyncio.run(main())
