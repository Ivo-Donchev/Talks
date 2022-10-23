import asyncio


def sync_func():
    print('Synchronous function execution')
    print('Synchronous function finish')


async def coroutine_func():
    print('Coroutine starts')

    sync_func()

    print('Coroutine finish')


async def main():
    await coroutine_func()

    await coroutine_func()


if __name__ == '__main__':
    asyncio.run(main())
