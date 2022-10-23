def func(id):
    total_iterations = 100000000
    step = total_iterations / 10

    for i in range(1, total_iterations):
        if i % step == 0:
            progress = (i / step) * 10
            print(
                f'Worker {id} reached {progress} %'
            )
