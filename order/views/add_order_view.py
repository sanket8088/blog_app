from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from order.models import Order, OrderProducts
from products.models import UserCart
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from order.serializer import PlaceOrderRequest


class PlaceOrderView(APIView):
    """Add address for user"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request):
        user = request.user
        req_data = request.data
        request_data = PlaceOrderRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        qs = Order.objects.create(user = user, billing_address = req_data["billing_address"], shipping_address = req_data["shipping_address"])
        cart_qs = UserCart.objects.filter(user = user)
        total_cost = 0
        for item in cart_qs:
            cost = float(item.product.price) * float(item.quantity)
            total_cost+=cost
            op_qs = OrderProducts.objects.create(order = qs, product = item.product, cost = item.product.price, quantity = item.quantity)
        UserCart.objects.filter(user = user).delete()
        return Response({"total_cost" : total_cost, "msg" : "Order placed"}, status = status.HTTP_200_OK)




