import threading
from common import Timer


def cpu_heavy():
    # String heavy operation
    result = ''

    for i in range(1000000):
        result += 'a'


def singlethreaded():
    for i in range(50):
        cpu_heavy()


def multithreaded():
    threads = []
    for i in range(50):
        thread = threading.Thread(target=cpu_heavy)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def main():
    print('Running....')

    with Timer('Single threaded'):
        singlethreaded()

    with Timer('Multiple threads'):
        multithreaded()


if __name__ == '__main__':
    main()
