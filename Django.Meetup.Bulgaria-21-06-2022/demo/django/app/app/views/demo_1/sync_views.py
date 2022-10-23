# type: ignore
import time
from django.http import HttpResponse
from django.contrib.auth.models import User


def func():
    print('1. Sleep for a second...')
    time.sleep(0.2)

    print('2. Query...')
    return list(User.objects.all())


def demo_1_sync(request):
    res = []

    for user in range(10000):
        res.append(func())

    return HttpResponse(f'Result: {len(res)}.')
