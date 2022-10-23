import asyncio
from asgiref.sync import sync_to_async

from django.contrib.auth.models import User
from django.utils.decorators import classonlymethod

from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response




class AsyncApiMixin:
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def handle_exception(self, exc):
        return super().handle_exception(exc)

    async def finalize_response(self, request, response, *args, **kwargs):
        return super().finalize_response(request, await response, *args, **kwargs)


class Demo2Api(
    AsyncApiMixin,
    APIView,
):
    class InputSerializer(serializers.Serializer):
        user = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all(),
        )

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        username = serializers.CharField()
        first_name = serializers.CharField()
        last_name = serializers.CharField()

    async def post(self, request):
        serializer = self.InputSerializer(data=request.data)

        # To make ORM queries async
        await sync_to_async(serializer.is_valid)(raise_exception=True)

        user = serializer.validated_data['user']

        return Response(self.OutputSerializer(user).data)
