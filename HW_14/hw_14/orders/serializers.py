from rest_framework import serializers
from .models import Order
from accounts.models import Customer, User
from card.models import Cart


class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Customerserializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class Cartserializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = Customerserializers()
    cart = Cartserializers()
    class Meta:
        model = Order
        fields = '__all__'


