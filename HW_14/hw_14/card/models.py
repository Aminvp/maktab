from django.db import models
from shop.models import Product

class Cart(models.Model):
    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items_product', null=True)

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return f'{self.price}-{self.quantity}'