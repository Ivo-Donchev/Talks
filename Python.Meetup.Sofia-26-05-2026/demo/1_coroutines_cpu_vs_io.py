import asyncio
import time


async def cpu_heavy_operation():
    start = time.perf_counter()
    result = 0

    while time.perf_counter() - start < 1.0:
        for i in range(10_000):
            result += (i * i) % 97

    return f"CPU operation completed ({result})"


async def io_heavy_operation():
    await asyncio.sleep(1.0)

    return "IO operation completed"


async def main():
    cpu_task_count = 10
    io_task_count = 1000

    start = time.perf_counter()
    await asyncio.gather(*(cpu_heavy_operation() for _ in range(cpu_task_count)))
    cpu_duration = time.perf_counter() - start

    print(f"CPU benchmark ({cpu_task_count} tasks): {cpu_duration:.3f}s")

    start = time.perf_counter()
    await asyncio.gather(*(io_heavy_operation() for _ in range(io_task_count)))
    io_duration = time.perf_counter() - start

    print(f"IO benchmark ({io_task_count} tasks): {io_duration:.3f}s")


if __name__ == "__main__":
    asyncio.run(main())
