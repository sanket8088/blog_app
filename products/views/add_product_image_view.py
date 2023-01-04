from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import  Products, UserCart, ProductReview
from order.models import Order, OrderProducts
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from products.serializer import AddProductReviewRequest
import boto3
from datetime import datetime
from django.conf import settings


class AddProductImage(APIView):
    """Add address for user"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def put(self, request, product_id):
        user = request.user
        request_file = request.FILES.get("image", None)
        now= datetime.now()
        time = now.strftime("%H:%M:%S")
        time = time.replace(":", "")
        file_name = time + "/" + request_file.name
        if request_file:
            if Products.objects.filter(id = product_id).exists():
                s3 = boto3.resource('s3', aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key= settings.AWS_SECRET_ACCESS_KEY,
                    endpoint_url = settings.ENDPOINT_URL)
                bucket = s3.Bucket(settings.BUCKET_NAME)
                bucket.put_object(Key=file_name, Body = request_file)

                file_url = settings.FILE_URL + file_name
                Products.objects.filter(id = product_id).update(image = file_url)
                return Response({"msg" : "Image updated"}, status = 200)
            else:
                return Response({"msg" : "Invalid product"}, status = 400)
        else:
            return Response({"msg" : "File not found"}, status = 400) 
        
       



# keyID:
# 00425b2cd0a7da40000000002
# keyName:
# blog-dev
# applicationKey:
# K004m553dxRZO3JR5xtcvnJbgmrGCuE