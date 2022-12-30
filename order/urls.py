from django.urls import path
from order.views import PlaceOrderView

urlpatterns = [
    path('', PlaceOrderView.as_view()),
]


# 127.0.0.1:8000/api/v1/order ---> 
# Create a new order and add all products from the cart to order products and empty the cart


# 127.0.0.1:8000/api/v1/order/product/<int:product_id>
# Create a new order and add all products from the product_id to order products.