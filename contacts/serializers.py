from rest_framework import serializers
from .models import Category, Contact
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "creator",
            "name",
            "surname",
            "phone",
            "email",
            "creation_date",
            "description",
            "category",
            "category_name",
            "image",
            "full_name",
        ]

    full_name = serializers.SerializerMethodField()
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    category_name = serializers.StringRelatedField(source="category")
    # id_category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(),
    #     source="category",
    # )

    def get_full_name(self, contact):
        return f"{contact.name} {contact.surname}"
