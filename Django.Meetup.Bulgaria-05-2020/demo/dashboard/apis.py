from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.db.models import Subquery, OuterRef, F, Value, ExpressionWrapper, DecimalField, Sum
from django.db.models.functions import Coalesce

from .models import Article, Author, Order, OrderContent, Invoice, InvoiceItem, HeavyModel


class Demo1Api(APIView):
    class ArticleSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=255)
        content = serializers.CharField(max_length=255)
        author_name = serializers.CharField(max_length=255, source='author.name')

    def get(self, request):
        """
        Get first 200 articles with the author_name
        """
        queryset = Article.objects.all()[:200]

        serializer = self.ArticleSerializer(queryset, many=True)

        return Response(data=serializer.data)


class Demo2Api(APIView):
    class InvoiceSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        total_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def get(self, request):
        queryset = Invoice.objects.all()

        serializer = self.InvoiceSerializer(
            queryset,
            many=True
        )

        return Response(data=serializer.data)


class Demo4Api(APIView):
    def get(self, request):
        price = 0

        for order in OrderContent.objects.all():
            price += order.price * order.quantity

        return Response(data={'price': price})


class Demo5Api(APIView):
    class InvoiceSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        is_expired = serializers.BooleanField()

    def attach_is_expired_dynamically(self, invoices):
        expiration_days = 2  # 2 days
        now = datetime.now().date()

        for invoice in invoices:
            is_expired = bool(invoice.date + timedelta(days=expiration_days) > now)
            invoice.is_expired = is_expired

        return invoices

    def get(self, request):
        invoices = Invoice.objects.all()

        invoices = self.attach_is_expired_dynamically(invoices)

        serializer = self.InvoiceSerializer(invoices, many=True)

        return Response(data=serializer.data)


class Demo6Api(APIView):
    def get(self, request):
        heavy_objects = list(HeavyModel.objects.all())
        import ipdb; ipdb.set_trace()

        return Response()
