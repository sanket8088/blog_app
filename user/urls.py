from django.urls import path
from user.views import UserSignUpView, UserLoginView, VerifyOtpView, FetchUserView, AddressView


urlpatterns = [
    path('', FetchUserView.as_view()),
    path('signup', UserSignUpView.as_view()),
    path('login', UserLoginView.as_view()),
    path('verify/otp', VerifyOtpView.as_view()),
    path('address', AddressView.as_view()),
]

# uuid


# 127.0.0.1:8000/api/v1/user/ --- > POST request to signup user -- {"email", "password", "first_name", "contact_number"}