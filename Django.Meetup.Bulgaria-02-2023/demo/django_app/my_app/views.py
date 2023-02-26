import uuid

from django.db import transaction
from django.views.generic import View
from django.http.response import HttpResponse
from django.contrib.auth.models import User


class CRUDView(View):
    # @transaction.atomic
    def get(
        self,
        request,
        create_queries_count,
        select_queries_count,
        update_queries_count,
        delete_queries_count
    ):
        for _ in range(create_queries_count):
            User.objects.create(username=uuid.uuid4())

        for _ in range(select_queries_count):
            list(User.objects.all())

        for _ in range(update_queries_count):
            User.objects.filter(id=-1).update(first_name='Test')

        for _ in range(delete_queries_count):
            User.objects.filter(id=-1).delete()

        return HttpResponse()
