# type: ignore
import asyncio
from asgiref.sync import sync_to_async

from django.http import HttpResponse
from django.contrib.auth.models import User


async def func():
    print('1. Sleep for a second...')
    await asyncio.sleep(0.2)

    print('2. Query...')
    return await sync_to_async(list)(User.objects.all())  # Trigger query


async def demo_1_async(request):
    res = []

    res = await asyncio.gather(
        *[
            func()
            for i in range(10000)
        ]
    )

    return HttpResponse(f'Result: {len(res)}')
