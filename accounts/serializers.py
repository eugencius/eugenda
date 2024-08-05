from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "confirm_password",
        ]

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate(self, attrs):
        super_validate = super().validate(attrs)

        first_name = attrs.get("first_name")
        last_name = attrs.get("last_name")
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        if first_name == last_name:
            raise serializers.ValidationError(
                {
                    "first_name": "Both name fields cannot be equal",
                    "last_name": "Both name fields cannot be equal",
                }
            )

        if password != confirm_password:
            raise serializers.ValidationError(
                {
                    "password": "Both password fields must be equal",
                    "confirm_password": "Both password fields must be equal",
                }
            )

        return super_validate
