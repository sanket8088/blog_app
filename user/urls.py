from django.urls import path
from user.views import UserSignUpView, UserLoginView, VerifyOtpView


urlpatterns = [
    path('', UserSignUpView.as_view()),
    path('login', UserLoginView.as_view()),
    path('verify/otp', VerifyOtpView.as_view()),
]


# 127.0.0.1:8000/api/v1/user/ --- > POST request to signup user -- {"email", "password", "first_name", "contact_number"}