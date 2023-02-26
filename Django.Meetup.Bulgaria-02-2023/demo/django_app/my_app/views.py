import uuid
import logging

from django.db import transaction
from django.views.generic import View
from django.http.response import HttpResponse
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


class CRUDView(View):
    def get(
        self,
        request,
        create_queries_count,
        select_queries_count,
        update_queries_count,
        delete_queries_count
    ):
        logger.debug('Executing INSERT queries')
        for _ in range(create_queries_count):
            User.objects.create(username=uuid.uuid4())

        logger.debug('Executing SELECT queries')
        for _ in range(select_queries_count):
            list(User.objects.only('id'))

        logger.debug('Executing UPDATE queries')
        for _ in range(update_queries_count):
            User.objects.filter(id=-1).update(first_name='Test')

        logger.debug('Executing DELETE queries')
        for _ in range(delete_queries_count):
            User.objects.filter(id=-1).delete()

        return HttpResponse()
