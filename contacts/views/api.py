from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Contact, Category
from ..serializers import ContactSerializer


@api_view(http_method_names=["POST"])
def contacts_api_create(request):
    pass


@api_view(http_method_names=["GET"])
def contacts_api_list(request):
    pass


@api_view(http_method_names=["PATCH"])
def contacts_api_edit(request, pk):
    pass


@api_view(http_method_names=["DELETE"])
def contacts_api_delete(request, pk):
    pass


@api_view()
def contacts_api_details(request, pk):
    pass
