import threading

COUNTER = 0


def increase_counter():
    global COUNTER
    print(f'Increasing counter from {COUNTER} to {COUNTER + 1}')
    COUNTER += 1


def main():
    print(f'Counter at the beginning: {COUNTER}')

    # Generate threads objects
    threads = [
        threading.Thread(target=increase_counter)
        for _ in range(50)
    ]

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print(f'Counter at the end: {COUNTER}')


if __name__ == '__main__':
    main()
