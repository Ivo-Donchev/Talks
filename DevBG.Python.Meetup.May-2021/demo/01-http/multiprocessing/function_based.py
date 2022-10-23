import requests
import multiprocessing
from common import Timer


def http_get(url):
    response = requests.get(url)
    print(f'HTTP GET {url} - response {response.status_code}')
    return response


def singleprocessed():
    for i in range(20):
        http_get('https://abv.bg')


def multiprocessed():
    processes = []

    # Start 10 separate processes
    for i in range(20):
        process = multiprocessing.Process(
            target=http_get,
            args=('https://abv.bg',)
        )

        process.start()
        processes.append(process)

    # Wait for all the threads to finish
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
