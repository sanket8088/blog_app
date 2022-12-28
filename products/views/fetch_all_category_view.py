from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializer import AddressRequest
from products.models import Categories
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.core.paginator import Paginator


# create a functionality to set default address
# provide a nickname to address


class FetchAllCategoriesView(APIView):
    """Add address for user"""
    permission_classes = [(IsAuthenticated)]

    def get(self, request):
        user = request.user
        category_qs = Categories.objects.filter(is_deleted = False)
        page = request.GET.get("p", 1)
        psz = request.GET.get("psz", 10)
        paginator_object = Paginator(category_qs, psz) #get total context of data, count, total_page_number
        object_list = paginator_object.page(page) #actual data of paginated form
        # import pdb; pdb.set_trace()
        page_info = {"count" : paginator_object.count, "total_pages" : paginator_object.num_pages, "cur_page" : page}
        if object_list.has_next():
            page_info["next"] = object_list.next_page_number()
        else:
            page_info["next"] = None
        if object_list.has_previous():
            page_info["previous"] = object_list.previous_page_number()
        else:
            page_info["previous"] = None

        resp = []
        for data in object_list:
            resp.append({"id" : data.id, "name" : data.name, "description" : data.description})
            
        return Response({"page_info" : page_info, "data" : resp}, status = 200)



# 1. url parameter - Mandatory
# 2. Query params - Non mandatory

# 21  1 1-10
#     2 11-20
#     3 21-30



