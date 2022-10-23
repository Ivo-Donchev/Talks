import multiprocessing
from common import Timer


def cpu_heavy():
    # String heavy operation
    result = ''

    for i in range(1000000):
        result += 'a'


class AsyncCPUHeavy(multiprocessing.Process):
    def run(self):
        cpu_heavy()


def singleprocessed():
    for i in range(50):
        cpu_heavy()


def multiprocessed():
    processes = []
    for i in range(50):
        process = AsyncCPUHeavy()
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


def main():
    print('Running....')

    with Timer('Single process'):
        singleprocessed()

    with Timer('Multiple processes'):
        multiprocessed()


if __name__ == '__main__':
    main()
