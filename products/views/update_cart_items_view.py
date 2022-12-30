from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializer import AddressRequest
from products.models import UserCart, Products
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.core.paginator import Paginator
from django.db import transaction
from products.serializer import UpdateCartRequest
from utils.error_msg import ACCESS_DENIED_MSG



class UpdateCartDataView(APIView):
    """Add address for user"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def put(self, request, cart_id):
        user = request.user
        req_data = request.data
        request_data = UpdateCartRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        user_access = self.verify_cart_access(cart_id, user)
        if user_access:
            UserCart.objects.filter(user=user, id = cart_id).update(quantity = req_data["quantity"])
            return Response({"msg" : "Cart item updated"}, status = status.HTTP_200_OK)
        else:   
            return Response(ACCESS_DENIED_MSG, status = status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, cart_id):
        user = request.user
        user_access = self.verify_cart_access(cart_id, user)
        if user_access:
            UserCart.objects.filter(user=user, id = cart_id).delete()
            return Response({"msg" : "Cart item deleted"}, status = status.HTTP_200_OK)
        else:
            return Response(ACCESS_DENIED_MSG, status = status.HTTP_401_UNAUTHORIZED)

    def verify_cart_access(self, cart_id, user):
        if UserCart.objects.filter(user=user, id = cart_id).exists():
            return True
        return False




