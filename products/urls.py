from django.urls import path
from products.views import (FetchAllCategoriesView, FetchAllProductsCategoryView, AddProductToCartView,
                            FetchCartDataView)


urlpatterns = [
    path('category', FetchAllCategoriesView.as_view()),
    path('category/<int:category_id>/product', FetchAllProductsCategoryView.as_view()),
    path('product/<int:product_id>/cart', AddProductToCartView.as_view()),
    path('cart', FetchCartDataView.as_view()),
]

# uuid


# 127.0.0.1:8000/api/v1/user/ --- > POST request to signup user -- {"email", "password", "first_name", "contact_number"}



# 127.0.0.1:8000/api/v1/products/category -- > all categories
# 127.0.0.1:8000/api/v1/products/category/<int:category_id>/product -- > all products inside that category
#  