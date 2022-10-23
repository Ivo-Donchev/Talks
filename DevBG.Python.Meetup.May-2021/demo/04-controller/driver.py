import time
import multiprocessing


def log(msg):
    print(msg)


class DriverProcess(multiprocessing.Process):
    def __init__(self, messages_queue, stop_signal):
        super(DriverProcess, self).__init__()
        self.messages_queue = messages_queue
        self.stop_signal = stop_signal

    def run(self):
        log('Starting driver process')

        # Gather device data
        while not self.stop_signal.is_set():
            time.sleep(1)

        log('Stopping driver process')
