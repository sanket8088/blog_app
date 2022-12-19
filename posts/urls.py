from django.urls import path
from posts.views import CreatePostView, GetUpdatePostView

urlpatterns = [
    path('', CreatePostView.as_view()),
    path('<int:post_id>', GetUpdatePostView.as_view()),
]


# 127.0.0.1:8000/api/v1/posts/ --> Create a post, GET request
#127.0.0.1:8000/api/v1/posts/<int:post_id> --> Get a post, Update a post and delete