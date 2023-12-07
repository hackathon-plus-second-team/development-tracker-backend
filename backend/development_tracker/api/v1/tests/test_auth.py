"""Tests for the endpoints 'auth' of 'Api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from api.v1.auth.serializers import AuthUserSignInSerilizer
from api.v1.auth.views import signin

User = get_user_model()


class SignInTestCase(APITestCase):
    """Tests for signin."""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )

    def test_signin(self):
        request_data = {"email": "test@example.com", "password": "testpassword"}
        serializer = AuthUserSignInSerilizer(data=request_data)
        serializer.is_valid(raise_exception=True)
        request = self.factory.post("api/v1/auth/signin/", serializer.validated_data)
        response = signin(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
