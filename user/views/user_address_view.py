from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializer import AddressRequest
from user.models import Address
from rest_framework.permissions import IsAuthenticated
from django.db import transaction



class AddressView(APIView):
    """Add address for user"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request):
        user = request.user
        req_data = request.data
        request_data = AddressRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        qs = Address.objects.create(street_address = req_data["street_address"], city = req_data["city"], 
                                    state = req_data["state"], pincode = req_data["pincode"], user = user)
        return Response({"id" : qs.id, "street_address" : qs.street_address}, status = 200)

    
    def get(self, request):
        user = request.user
        qs = Address.objects.filter(user = user, is_deleted= False)
        resp = []
        for address in qs:
            resp.append({"id" : address.id, "street_address" : address.street_address})
        return Response({"data" : resp}, status = 200)




