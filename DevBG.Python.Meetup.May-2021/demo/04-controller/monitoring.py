import time
import multiprocessing


def log(msg):
    print(msg)


class MonitoringProcess(multiprocessing.Process):
    def __init__(self, messages_queue, stop_signal):
        super(MonitoringProcess, self).__init__()
        self.messages_queue = messages_queue
        self.stop_signal = stop_signal

    def run(self):
        log('Starting monitoring process')

        while not self.stop_signal.is_set():
            time.sleep(1)

            while not self.messages_queue.empty():
                msg = self.messages_queue.get()
                if msg == 'monitoring/info':
                    print('Gathering monitoring info...')

        log('Stopping monitoring process')
