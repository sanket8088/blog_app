from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializer import AddressRequest
from user.models import Address
from rest_framework.permissions import IsAuthenticated
from django.db import transaction


# create a functionality to set default address
# provide a nickname to address


class AddressDefaultView(APIView):
    """Add address for user"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def put(self, request, address_id):
        user = request.user
        if Address.objects.filter(user = user, id = address_id).exists():
            Address.objects.filter(user = user).update(is_default = False)
            Address.objects.filter(id = address_id).update(is_default = True)
            return Response({"msg" : "Updated successfully"}, status = 200)
        else:
            return Response({"msg" : "Access denied"}, status = 400)




