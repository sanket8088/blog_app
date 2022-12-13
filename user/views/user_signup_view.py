from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User, OtpUser
from user.serializer import SignUpRequest, UserSerializer


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
        # otp = 6 random digits
        # user_instance
        # Otp.objects.create(otp = self.generate_otp(), user= user_instance)
        return Response(resp, status = 200)
    
    def generate_response(self, instance):
        resp = {}
        resp["id"] = instance.id
        resp["email"] = instance.email
        return resp


#Any post request >> Create a serializer for it >> Just to validate required keys are present