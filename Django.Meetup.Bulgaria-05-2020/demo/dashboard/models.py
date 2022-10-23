from django.db.models import (
    Model,
    CharField,
    IntegerField,
    TextField,
    ForeignKey,
    CASCADE,
    DecimalField,
    OneToOneField,
    DateField,
    QuerySet
)

from decimal import Decimal


class Author(Model):
    name = CharField(max_length=255)
    age = IntegerField()

    @property
    def articles_count(self):
        return self.articles.count()


class Article(Model):
    title = CharField(max_length=255)
    content = TextField()
    author = ForeignKey(
        Author,
        related_name='articles',
        on_delete=CASCADE
    )


class OrderContent(Model):
    quantity = IntegerField()
    price = DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.quantity * self.price


class Order(Model):
    client = ForeignKey(
        Author,
        on_delete=CASCADE,
        related_name='orders',
        blank=True,
        null=True,
        default=None
    )
    content = OneToOneField(
        OrderContent,
        on_delete=CASCADE,
    )


class InvoiceItemQuerySet(QuerySet):
    def map(self, func):
        class MyIterableClass(self._iterable_class):
            def __iter__(self):
                for obj in super(self.__class__, self).__iter__():
                    yield func(obj)

        qs = self._clone()
        qs._iterable_class = MyIterableClass

        return qs


class InvoiceQuerySet(QuerySet):
    def collect(self):
        return self.all()


class Invoice(Model):
    objects = InvoiceQuerySet.as_manager()

    date = DateField()
    description = TextField()

    @property
    def total_price(self):
        price = 0

        for item in self.items.all():
            price += item.price

        return price


class InvoiceItem(Model):
    objects = InvoiceItemQuerySet.as_manager()

    invoice = ForeignKey(
        Invoice,
        on_delete=CASCADE,
        related_name='items',
    )

    quantity = IntegerField()
    unit_price = DecimalField(max_digits=10, decimal_places=2)
    tax = DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.2')
    )

    @property
    def price(self):
        return self.quantity * self.unit_price * (1 + self.tax)


class HeavyModel(Model):
    dec_field_1 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_2 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_3 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_4 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_5 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_6 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_7 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_8 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_9 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_10 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_11 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_12 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_13 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_14 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_15 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_16 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_17 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_18 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_19 = DecimalField(max_digits=10, decimal_places=2)
    dec_field_20 = DecimalField(max_digits=10, decimal_places=2)

    text_field_1 = TextField()
    text_field_2 = TextField()
    text_field_3 = TextField()
    text_field_4 = TextField()
    text_field_5 = TextField()
    text_field_6 = TextField()
    text_field_7 = TextField()
    text_field_8 = TextField()
    text_field_9 = TextField()
    text_field_10 = TextField()
    text_field_11 = TextField()
    text_field_12 = TextField()
    text_field_13 = TextField()
    text_field_14 = TextField()
    text_field_15 = TextField()
    text_field_16 = TextField()
    text_field_17 = TextField()
    text_field_18 = TextField()
    text_field_19 = TextField()
    text_field_20 = TextField()
