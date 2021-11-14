

from django.db import models
from card.models import Cart

class User(models.Model):
    username = models.CharField(max_length=25, null=True)
    password = models.CharField(max_length=18, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username





class Customer(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer', null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10, unique=True)
    country = models.CharField(max_length=50)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name='customer_cart', null=True)

    def __str__(self):
        return self.email

