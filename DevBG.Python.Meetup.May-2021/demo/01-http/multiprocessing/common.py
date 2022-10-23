from time import time


class Timer(object):
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time()

    def __exit__(self, type, value, traceback):
        self.end = time()

        print(f"{self.message}: {self.end - self.start}")
