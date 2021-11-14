from django.db import models
from accounts.models import Customer
from card.models import Cart


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders_customer', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders', null=True)


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.customer}-{self.id}'


