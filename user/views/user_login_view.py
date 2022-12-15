from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializer import LoginRequest
from user.models import User
from rest_framework.authtoken.models import Token


class UserLoginView(APIView):
    """Login functionality for user"""

    def post(self, request):
        # email and password
        req_data = request.data
        request_data = LoginRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        email = req_data["email"]
        password = req_data["password"]
        user_qs = User.objects.filter(email = email)
        if user_qs.exists():
            user_instance = user_qs[0]
            if user_instance.otp_verified:
                password_check = user_instance.check_password(password)
                if password_check:
                    token, created = Token.objects.get_or_create(user = user_instance)
                    print(token)
                    return Response({"key" : token.key}, status = 200)
                else:
                    return Response({"msg" : "Invalid password"}, status = 400)
            else:
                return Response({"msg" : "User not activated"}, status = 400)
        else:
            return Response({"msg" : "Invalid email"}, status = 400)
        