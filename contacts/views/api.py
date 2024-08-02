from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from ..models import Contact, Category
from ..serializers import ContactSerializer


class ContactsListAPI(APIView):
    def get(self, request):
        user = request.user

        contacts = (
            Contact.objects.filter(creator=user)
            .order_by("-id")
            .select_related("category")
        )
        serializer = ContactSerializer(instance=contacts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        category_id = request.data.get("category_id")

        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=user, category_id=category_id)

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class ContactsDetailsAPI(APIView):
    def get_contact(self, user, pk):
        contact = Contact.objects.filter(creator=user, pk=pk).first()

        if not contact:
            raise NotFound()

        return contact

    def get(self, request, pk):
        user = request.user
        contact = self.get_contact(user, pk)

        serializer = ContactSerializer(instance=contact, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user = request.user
        contact = self.get_contact(user, pk)

        serializer = ContactSerializer(
            instance=contact,
            data=request.data,
            many=False,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = request.user
        self.get_contact(user, pk).delete()
        return Response(status=status.HTTP_200_OK)
