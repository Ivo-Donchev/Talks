from django.urls import path, include
from django.conf import settings
from .apis import Demo1Api, Demo2Api, Demo4Api, Demo5Api, Demo6Api

urlpatterns = [
    path('1/', Demo1Api.as_view()),
    path('2/', Demo2Api.as_view()),
    path('4/', Demo4Api.as_view()),
    path('5/', Demo5Api.as_view()),
    path('6/', Demo6Api.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
