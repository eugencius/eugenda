from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Contact, Category
from ..serializers import ContactSerializer


@api_view(http_method_names=["POST"])
def contacts_api_create(request):
    user = request.user
    category_id = request.data.get("category_id")

    serializer = ContactSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(creator=user, category_id=category_id)

    return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["GET"])
def contacts_api_list(request):
    user = request.user

    contacts = (
        Contact.objects.filter(creator=user).order_by("-id").select_related("category")
    )
    serializer = ContactSerializer(instance=contacts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["PATCH"])
def contacts_api_edit(request, pk):
    user = request.user

    contact = Contact.objects.filter(creator=user, pk=pk).first()
    if not contact:
        return Response({"detail": "Eita!"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ContactSerializer(
        instance=contact,
        data=request.data,
        many=False,
        partial=True,
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["DELETE"])
def contacts_api_delete(request, pk):
    user = request.user
    contact = Contact.objects.filter(creator=user, pk=pk).first()

    if not contact:
        return Response({"detail": "Eita!"}, status=status.HTTP_404_NOT_FOUND)

    contact.delete()
    return Response(status=status.HTTP_200_OK)


@api_view()
def contacts_api_details(request, pk):
    user = request.user

    contact = Contact.objects.filter(creator=user, pk=pk).first()
    if not contact:
        return Response({"detail": "Eita!"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ContactSerializer(instance=contact, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
