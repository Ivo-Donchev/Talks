import time


def func(id):
    print(f'Worker {id} started')
    time.sleep(2)
    print(f'Worker {id} finished')
