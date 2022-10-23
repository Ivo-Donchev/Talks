import multiprocessing
from utils import func


def main():
    processes = [
        multiprocessing.Process(
            target=func,
            args=(i,)
        )
        for i in range(1, 5)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    main()
