import time
import asyncio


async def bad_coroutine():
    for i in range(5):
        print(f'Bad coroutine sleeping  {i}')
        time.sleep(1)


async def good_corotine(id):
    for i in range(5):
        print(f'Good coroutine {id} sleeping - {i}')
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(
        *[
            good_corotine(i)
            for i in range(1000)
        ],
        bad_coroutine(),
    )


if __name__ == '__main__':
    asyncio.run(main())
