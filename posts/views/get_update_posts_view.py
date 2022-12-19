from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import UserPosts
from posts.serializer import AddPostsRequest
from rest_framework.permissions import IsAuthenticated


class GetUpdatePostView(APIView):
    permission_classes = [(IsAuthenticated)]
    """Get, update and delete posts for user"""
        
    def get(self, request, post_id):
        """Get posts of user"""

        user = request.user
        qs = UserPosts.objects.filter(id = post_id)
        resp = []
        for data in qs:
            resp.append({"id" : data.id, "title" : data.title, "description" : data.description, "created_at" : data.created_at})
        return Response({"data" : resp}, status = 200)
