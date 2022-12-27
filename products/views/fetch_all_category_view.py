from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializer import AddressRequest
from products.models import Categories
from rest_framework.permissions import IsAuthenticated
from django.db import transaction


# create a functionality to set default address
# provide a nickname to address


class FetchAllCategoriesView(APIView):
    """Add address for user"""
    permission_classes = [(IsAuthenticated)]

    def get(self, request):
        user = request.user
        category_qs = Categories.objects.filter(is_deleted = False)
        resp = []
        for category in category_qs:
            resp.append({"id" : category.id, "name" : category.name, "description" : category.description})
        return Response({"data" : resp}, status = 200)




