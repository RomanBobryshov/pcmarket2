from django.db import models
from pcmarket2.apps.products.models import Product
from django.db.models.expressions import Combinable


class Order(models.Model):
    id = models.UUIDField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.BigIntegerField(verbose_name='Номер телефону', blank=True, null=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Закази'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.objects.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.CharField ('Ціна товару:', max_length= 250)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(Order.id)

    def get_cost(self):
        pass
