from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import OrderSerializer
from .models import Order

@api_view()
def posts(request):
    orders = Order.objects.all()
    ser_data = OrderSerializer(posts, many=True)
    return Response(ser_data.data)
