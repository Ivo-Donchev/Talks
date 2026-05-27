import sys
from concurrent.futures import ThreadPoolExecutor
import time


def cpu_heavy_operation():
    start = time.thread_time()
    result = 0

    while time.thread_time() - start < 1.0:
        for i in range(10_000):
            result += (i * i) % 97

    return f"CPU operation completed ({result})"


def io_heavy_operation():
    time.sleep(1.0)

    return "IO operation completed"


def run_with_threads(task_count, operation):
    with ThreadPoolExecutor() as executor:
        list(executor.map(lambda _: operation(), range(task_count)))


def main():
    cpu_task_count = 10
    io_task_count = 100

    start = time.perf_counter()
    run_with_threads(cpu_task_count, cpu_heavy_operation)
    cpu_duration = time.perf_counter() - start

    print(f"CPU benchmark ({cpu_task_count} tasks): {cpu_duration:.3f}s")

    start = time.perf_counter()
    run_with_threads(io_task_count, io_heavy_operation)
    io_duration = time.perf_counter() - start

    print(f"IO benchmark ({io_task_count} tasks): {io_duration:.3f}s")


if __name__ == "__main__":
    print(
        "🔒 GIL ENABLED:",
        "✅" if sys._is_gil_enabled() else "❌",
    )
    main()
