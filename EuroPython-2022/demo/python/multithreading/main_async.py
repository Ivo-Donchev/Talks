import threading
from utils import func


def main():
    threads = [
        threading.Thread(
            target=func,
            args=(i,)
        )
        for i in range(1, 5)
    ]

    print('Starting threads...')

    for thread in threads:
        thread.start()

    print('Waiting for threads to finish...')

    for thread in threads:
        thread.join()

    print('Done')


if __name__ == '__main__':
    main()
