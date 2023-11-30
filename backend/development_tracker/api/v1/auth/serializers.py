"""Serializers for the endpoints 'auth' of 'Api' application v1."""

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from rest_framework import serializers

User = get_user_model()


class AuthUserSignInSerilizer(serializers.Serializer):
    """Serializer for working with signin requests."""

    email = serializers.EmailField()
    password = serializers.CharField()

    default_error_messages = {
        "invalid_password": "Invalid password.",
    }

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = get_object_or_404(User, email=email)

        if not check_password(password, user.password):
            raise serializers.ValidationError(
                {"detail": self.error_messages["invalid_password"]}
            )

        return data
