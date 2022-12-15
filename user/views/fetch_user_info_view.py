from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from rest_framework.permissions import IsAuthenticated


class FetchUserView(APIView):
    """Login functionality for user"""

    permission_classes = [(IsAuthenticated)]

    def get(self, request):
        # email and password
        user = request.user
        return Response({"id" : user.id, "name" : user.first_name, "email" : user.email}, status = 200)
        