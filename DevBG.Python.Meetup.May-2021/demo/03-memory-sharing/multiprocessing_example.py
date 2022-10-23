import multiprocessing

COUNTER = 0


def increase_counter():
    global COUNTER
    print(f'Increasing counter from {COUNTER} to {COUNTER + 1}')
    COUNTER += 1


def main():
    print(f'Counter at the beginning: {COUNTER}')

    # Generate processes objects
    processes = [
        multiprocessing.Process(target=increase_counter)
        for _ in range(50)
    ]

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print(f'Counter at the end: {COUNTER}')


if __name__ == '__main__':
    main()
