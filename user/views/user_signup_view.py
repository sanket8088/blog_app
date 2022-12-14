from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User, OtpUser
from user.serializer import SignUpRequest, UserSerializer
import random


class UserSignUpView(APIView):

    def post(self,request):
        req_data = request.data
        request_data = SignUpRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        if User.objects.filter(email = req_data["email"]).exists():
            return Response({"msg" : "Email already exists"}, status = 400)
        user_instance = UserSerializer.create(req_data)
        resp = self.generate_response(user_instance)
        # create a entry point for adding otp
        otp_val = self.generate_otp()
        OtpUser.objects.create(otp_value = otp_val, user= user_instance)
        return Response(resp, status = 200)
    
    def generate_response(self, instance):
        resp = {}
        resp["id"] = instance.id
        resp["email"] = instance.email
        return resp

    def generate_otp(self):
        return random.randint(100000, 999999)

#Any post request >> Create a serializer for it >> Just to validate required keys are present