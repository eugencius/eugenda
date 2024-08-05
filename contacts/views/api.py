from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Contact
from ..permissions import IsOwner
from ..serializers import ContactSerializer


class FilterQuerysetUser:
    def get_queryset(self):
        qs = super().get_queryset()

        user = self.request.user
        qs = qs.filter(creator=user)

        return qs


class ContactsViewsetAPI(FilterQuerysetUser, ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        qs = super().get_queryset().order_by("-id")
        return qs

    def create(self, request, *args, **kwargs):
        user = request.user

        contact = ContactSerializer(
            data=request.data,
            partial=True,
        )
        contact.is_valid(raise_exception=True)
        contact.save(creator=user)

        return Response(contact.data, status=status.HTTP_201_CREATED)
