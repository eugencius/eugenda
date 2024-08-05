from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class RegisterUserAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = [
        "post",
    ]
