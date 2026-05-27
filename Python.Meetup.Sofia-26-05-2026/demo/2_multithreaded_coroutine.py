import sys
import asyncio

import functools


def threaded_coroutine(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        return await asyncio.to_thread(func, *args, **kwargs)

    return wrapper


@threaded_coroutine
def cpu_heavy_operation():
    result = ""
    for i in range(50000000):
        result += str(i)
        result = result[-100:]

    return result


async def main():
    tasks = [cpu_heavy_operation() for _ in range(13)]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    print(
        "🔒 GIL ENABLED:",
        "✅" if sys._is_gil_enabled() else "❌",
    )
    asyncio.run(main())
