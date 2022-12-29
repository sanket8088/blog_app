from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import  Products, UserCart
from rest_framework.permissions import IsAuthenticated
from django.db import transaction


class AddProductToCartView(APIView):
    """Add address for user"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request, product_id):
        user = request.user
        print(user)
        if Products.objects.filter(id = product_id).exists():
            # if this data with this user_id exists update the count
            cart_qs = UserCart.objects.filter(user = user, product_id= product_id)
            if cart_qs.exists():
                quantity = cart_qs[0].quantity
                UserCart.objects.filter(user = user, product_id= product_id).update(quantity = quantity+1)
                cart_qs = cart_qs[0]
            else:
                cart_qs = UserCart.objects.create(user = user, product_id= product_id)
            return Response({"id" : cart_qs.id, "name" : cart_qs.product.name}, status = 200)
        else:
            return Response({"msg" : "Invalid product"}, status = 400)




