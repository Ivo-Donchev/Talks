from django.contrib import admin
from django.urls import path

from .views import (
    async_view,
    view_with_threading,
    view_with_multiprocessing,
    demo,
    demo_async,
    demo_1_sync,
    demo_1_async,
    Demo2Api,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('multiprocessing/', view_with_multiprocessing),
    path('threading/', view_with_threading),
    path('async/', async_view),
    path('demo/', demo),
    path('demo/async/', demo_async),
    path('demo/1/sync/', demo_1_sync),
    path('demo/1/async/', demo_1_async),
    path('demo/2/', Demo2Api.as_view()),
]
